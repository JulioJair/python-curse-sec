from sqlite_conn import SQLite_controller
import socket
import threading
import logging
import sys

FORMAT = 'utf-8'

class Pki_rsa:
    def __init__(self):
        from rsa import key
        (pub_key, priv_key) = key.newkeys(256)
        self.pub_key = pub_key
        self.__priv_key = priv_key

    def gen_keys(self):
        """Generate new keys for user, maybe in case of lost"""
        from rsa import key
        (pub_key, priv_key) = key.newkeys(256)
        self.pub_key = pub_key
        self.priv_key = priv_key

    def encrypt(self, message, pub_key_receiver):
        """Encrypt with the recipient public key"""
        from rsa import encrypt
        encoded_message = message.encode(FORMAT)
        encrypted_message = encrypt(encoded_message, pub_key_receiver)
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Decrypt with personal private key"""
        from rsa import decrypt
        encoded_message = decrypt(encrypted_message, self.__priv_key)
        message = encoded_message.decode(FORMAT)
        return message

    def key_to_keystring(self, key):
        return key.save_pkcs1(format="PEM")

    def keystring_to_key(self, keystring):
        import rsa
        return rsa.key.PublicKey.load_pkcs1(keystring, format="PEM")

class ClientMessenger:
    def __init__(self, host, port):
        """

        :param host:
        :param port:
        """
        self.__HOST = host
        self.__PORT = port
        self.user = None
        self.contact = None
        self.client = None
        self.user_is_chatting = False
        self.keys = Pki_rsa()
        self.contact_public_key = None
        print(f'Keys generated\n{self.keys.pub_key}')

        # DB connection wait until user start chatting
        self.db = None

    def receive(self):

        """
        Connect to server and look for a contact to chat
        Request user and contact, and start a thread with encrypted chat

        :return:
        """
        while not self.user_is_chatting:
            try:
                # Receive Message From Server
                data = self.client.recv(1024).decode(FORMAT)
                # If 'USER' Send User
                if data == 'USER':
                    self.user = input(f'¿Cual es tu usuario? ').upper()
                    self.client.sendall(self.user.encode(FORMAT))
                elif data == 'PUBLIC_KEY':
                    pkstring = self.keys.pub_key.save_pkcs1(format="PEM")
                    self.client.sendall(pkstring)
                elif data == 'CONTACT':
                    self.contact = input(f'¿Con quien deseas hablar? ').upper()
                    self.client.sendall(self.contact.encode(FORMAT))
                elif data == 'ENCRYPT':
                    self.user_is_chatting = True
                elif data == 'REMOVED':
                    self.client.close()
                    sys.exit()
                else:
                    print(data)
            except:
                # Close Connection When Error
                print("An error occured!")
                self.client.close()
                sys.exit()

        if self.user_is_chatting:
            chat_thread = threading.Thread(target=self.chat)
            chat_thread.start()

    def chat(self):
        """
        Encrypted chat, only the receiver can decrypt the message
        if messagge == salir -> Close this chat

        :return:
        """
        # * Table definition
        conversation = {
            self.contact: {
                "encrypted_msg": "text",
                "decrypted_msg": "text"}}

        # DB connection
        self.db_name = f'chats_{self.user}.db'
        self.db = SQLite_controller(self.db_name, conversation)

        # Get the contact public key
        data = self.client.recv(1024)
        self.contact_public_key = self.keys.keystring_to_key(data)
        print(f'{self.contact} public key\n {self.contact_public_key}')
        while self.user_is_chatting:
            try:
                # RECEIVING AND DECRYPTING
                data = self.client.recv(1024)
                try:
                    encrypted_message = data
                    data = self.keys.decrypt(data)
                    # Store messages
                    self.db.insert(self.contact, (encrypted_message, data))
                except:
                    print("Not a valid encrypted data")
                    data = data.decode(FORMAT)
                finally:
                    print(data)

                # SENDING
                msg = input(f'YOU: ')
                if msg == 'salir':
                    self.send_encrypted_msg(f"\n* {self.user} left! *\n")

                    # Close the client session
                    self.client.close()
                    sys.exit()
                else:
                    msg = self.user + ': ' + msg
                    self.send_encrypted_msg(msg)
            except:
                # Close the current session and exit the program
                print("Connection with server lost.")
                print("Erasing data from this client..")
                # Delete local database
                import os
                os.remove(self.db_name)
                print("Closing this session...")
                self.client.close()
                sys.exit()

    def send_encrypted_msg(self, message):
        encrypted_message = self.keys.encrypt(message, self.contact_public_key)
        self.db.insert(self.contact, (encrypted_message, message))
        self.client.sendall(encrypted_message)

    # Starting Client
    def start(self):
        """
        Create the socket client

        :return:
        """
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.__HOST, self.__PORT))

        # Starting Thread For Receiving
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        # print(f"LOGS FILE -> '{self.user}_{self.__HOST}:{self.__PORT}.log'")
        # # Create and configure logger
        # LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        # logging.basicConfig(filename=f"{self.user}/{self.__HOST}:{self.__PORT}.log", level=logging.DEBUG,
        #                     format=LOG_FORMAT,
        #                     filemode='w')
        # self.logger = logging.getLogger()


if __name__ == '__main__':
    # Connection Data
    LOCALHOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050  # Port to listen on (non-privileged ports are > 1023)
    my_client = ClientMessenger(LOCALHOST, PORT)
    my_client.start()

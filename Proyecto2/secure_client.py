from pki_rsa import Pki_rsa
import socket
import threading
import logging
import sys

FORMAT = 'utf-8'


class ClientMessenger:
    def __init__(self, host, port):
        self.__HOST = host
        self.__PORT = port
        self.user = None
        self.contact = None
        self.client = None
        self.user_is_not_chatting = True
        self.keys = Pki_rsa()
        self.contact_public_key = None
        print(f'Keys generated\n{self.keys.pub_key}')

    def receive(self):
        while self.user_is_not_chatting:
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
                    self.user_is_not_chatting = False
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

        if self.user_is_not_chatting == False:
            # Get the contact public key
            data = self.client.recv(1024)
            self.contact_public_key = self.keys.keystring_to_key(data)
            print(f'{self.contact} public key\n {self.contact_public_key}')

        while self.user_is_not_chatting == False:
            try:
                # RECEIVING AND DECRYPTING
                data = self.client.recv(1024)
                try:
                    data = self.keys.decrypt(data)
                except:
                    pass
                finally:
                    print(data)
                # SENDING
                msg = input(f'YOU: ')
                msg = self.user + ': ' + msg
                self.send_encrypted_msg(msg)
            except:
                print("An error ocurred while chatting")

                self.client.close()
                sys.exit()

    def send_encrypted_msg(self, message):
        encrypted_message = self.keys.encrypt(message, self.contact_public_key)
        self.client.sendall(encrypted_message)

    # Starting Client
    def start(self):
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
    PORT = 5055  # Port to listen on (non-privileged ports are > 1023)
    my_client = ClientMessenger(LOCALHOST, PORT)
    my_client.start()

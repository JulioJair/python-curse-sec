from sqlite_conn import SQLite_controller
import socket
import threading
import logging
import time

FORMAT = 'utf-8'


class ServerMessenger:
    def __init__(self, host, port):
        self.__HOST = host
        self.__PORT = port

        # Create and configure logger
        print(f"LOGS FILE -> '{self.__HOST}:{self.__PORT}.log'")
        LOG_FORMAT = "%(levelname)s - %(message)s"
        logging.basicConfig(filename=f"{self.__HOST}:{self.__PORT}.log", level=logging.DEBUG, format=LOG_FORMAT,
                            filemode='w')
        self.logger = logging.getLogger()

        # * Table definition
        keys_table = {
            "users_pub_keys": {
                "user": "text",
                "public_key": "text"}}

        # DB connection
        self.db = SQLite_controller('secure_server.db', keys_table)

        # DB for Users
        self.available_users = dict()
        self.logger.debug(f'Available users: {self.available_users.keys()}')

        self.public_keys = dict()
        self.logger.debug(f'Public keys saved from {self.public_keys.keys()}')

        # Create socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.__HOST, self.__PORT))
        self.server_socket.listen(10)
        self.logger.info(f'[LISTENING] Server is listening on {self.__HOST}:{self.__PORT}')

        thread_accept_client = threading.Thread(target=self.accept_client())
        thread_accept_client.start()

    def accept_client(self):
        """
            Register the user to make him available to chat

        :return:
        """
        while True:
            # Accept Connection
            conn, addr = self.server_socket.accept()

            self.logger.info(f'[NEW CONNECTION] {conn}')

            # Request And Store user and connection
            user_not_accepted = True
            while user_not_accepted:
                self.logger.debug(f'{self.available_users.keys()}')
                self.logger.debug(f'Requesting user')
                conn.sendall('USER'.encode(FORMAT))

                self.logger.debug(f'Waiting for user')
                user = conn.recv(1024).decode(FORMAT)
                self.logger.debug(f'User received: {user} ')

                try:
                    if user in self.available_users.keys():
                        conn.sendall(f"{user} is already taken".encode(FORMAT))

                    elif user not in self.available_users.keys():
                        # User accepted
                        self.available_users.update({user: conn})
                        print(f"{user} : {conn} is now available")
                        conn.sendall(f"{user}, you are available now".encode(FORMAT))
                        user_not_accepted = False
                except:
                    print("Error requesting user")
                finally:
                    self.logger.debug(f'USERS AVAILABLE: \n{self.available_users.keys()}')

            # Request public key from the valid user
            try:
                time.sleep(0.5)
                conn.sendall('PUBLIC_KEY'.encode(FORMAT))
                self.logger.debug(f'Waiting for public key from {user}')
                public_key = conn.recv(1024).decode(FORMAT)
                self.logger.debug(f'Public key received: {public_key}')
                self.public_keys.update({user: public_key})
                self.logger.debug(f'KEYS: \n{self.public_keys}')
            except:
                print("Error requesting public key")

            # Establish connection between clients
            thread_handle_client = threading.Thread(target=self.handle_client, args=(user, conn))
            thread_handle_client.start()

    def handle_client(self, user, conn):
        """
        Ask the user with whom want to talk to

        :param user: a valid username for the client
        :param conn: connection object from the user
        :return:
        """
        self.logger.info(f'[HANDLING] {user}')
        user_not_chatting = True
        while user_not_chatting:
            self.logger.debug(f'Sending available users to {user}')
            conn.sendall(f'Usuarios disponibles: {list(self.available_users.keys())}'.encode(FORMAT))
            time.sleep(0.5)
            conn.sendall('CONTACT'.encode(FORMAT))
            self.logger.debug(f'waiting for user')
            receiver = conn.recv(1024).decode(FORMAT)
            self.logger.debug(f'{user} is trying to talk with {receiver}')
            try:
                if receiver == 'salir':
                    conn.sendall('REMOVED'.encode(FORMAT))
                    del self.available_users[user]
                    self.logger.info(f'{user} removed -> {list(self.available_users.keys())}')
                    break
                elif receiver == user:
                    self.logger.error(f"user and receiver can't be the same")
                    conn.sendall(f'¡No puedes hablar contigo mismo!'.encode(FORMAT))
                elif receiver not in self.available_users.keys():
                    self.logger.error(f'{receiver} is not an available user to connect')
                    conn.sendall(f'{receiver} no esta disponible'.encode(FORMAT))
                elif receiver in self.available_users.keys():
                    self.logger.info(f'Establishing connection between {user} and {receiver}')
                    conn.sendall(f'OK!'.encode(FORMAT))
                    user_not_chatting = False
            except:
                print("Error connecting to a receiver")

        if user_not_chatting == False:
            # Settings for the encrypted chat
            receiver_conn = self.available_users.get(receiver)
            self.logger.info(f'[CHAT ESTABLISHED] {user} is sending messages to {receiver}')
            self.logger.info(f'{receiver} conn is: {receiver_conn}')
            conn.sendall(f'Tu conexi�n con {receiver} esta cifrada'.encode(FORMAT))
            receiver_conn.sendall(f'\n*** {user} esta comunicandose contigo ***'.encode(FORMAT))
            time.sleep(0.5)
            conn.sendall('ENCRYPT'.encode(FORMAT))

            # Send the receiver public key to the user
            receiver_pub_key = self.public_keys.get(receiver)
            self.logger.info(f'{receiver} {receiver_pub_key}')
            print(f'{receiver} {receiver_pub_key}')
            time.sleep(0.5)
            conn.sendall(str(receiver_pub_key).encode(FORMAT))

        while user_not_chatting == False:
            try:
                message = conn.recv(1024)
                # In case of unexpected lost of connection
                if message == b'':
                    self.logger.info(f'{user} is gone!')
                    receiver_conn.sendall(f'\n*** {user} left the chat! ***\n'.encode(FORMAT))
                    del self.available_users[user]
                    self.logger.info(f'{user} removed, online users: -> {list(self.available_users.keys())}')
                    conn.close()
                    break
                # Just send the encrypted data to the target
                else:
                    print(f'{user} to {receiver}: ')
                    print(message)
                    receiver_conn.sendall(message)
            # If connection with user is lost, remove their connection
            except:
                del self.available_users[user]
                self.logger.info(f'{user} removed, online users -> {list(self.available_users.keys())}')


if __name__ == '__main__':
    # Connection Data
    LOCALHOST = socket.gethostbyname(socket.gethostname())
    PORT = 5055  # Port to listen on (non-privileged ports are > 1023)

    my_server = ServerMessenger(LOCALHOST, PORT)
    # my_server.start_listen()

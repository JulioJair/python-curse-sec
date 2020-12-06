from pki_rsa import Pki_rsa
import socket
import threading
import logging


class Server_messenger:
    def __init__(self, host, port):
        self.__HOST = host
        self.__PORT = port
        self.FORMAT = 'utf-8'
        # DB for Users
        self.available_users = {}

    # Starting Server
    def start_listen(self):
        print(f"LOGS FILE -> '{self.__HOST}:{self.__PORT}.log'")
        # Create and configure logger
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename=f"{self.__HOST}:{self.__PORT}.log", level=logging.DEBUG, format=LOG_FORMAT,
                            filemode='w')
        logger = logging.getLogger()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__HOST, self.__PORT))
            s.listen()
            logger.info(f'[LISTENING] Server is listening on {self.__HOST}:{self.__PORT}')

            conn, addr = s.accept()
            self.clients
            # with conn:
            #     self.listen_client(conn, addr)


if __name__ == '__main__':
    # Connection Data
    LOCALHOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050  # Port to listen on (non-privileged ports are > 1023)

    my_server = Server_messenger(LOCALHOST, PORT)
    my_server.start_listen()

from pki_rsa import Pki_rsa
import socket
import threading
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log_python.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

LOCALHOST = socket.gethostbyname(socket.gethostname())


class Server:
    def __init__(self, host, port):
        self.__HOST = host
        self.__PORT = port

    # Starting Server
    def start_listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__HOST, self.__PORT))
            s.listen()
            logger.info(f'[LISTENING] Server is listening on {self.__HOST}')
            conn, addr = s.accept()
            with conn:

            self.listen_client(conn, addr)


if __name__ == '__main__':
    LOCALHOST = socket.gethostbyname(socket.gethostname())
    PORT = 5051  # Port to listen on (non-privileged ports are > 1023)
    my_server = Server(LOCALHOST, PORT)
    my_server.start_listen()

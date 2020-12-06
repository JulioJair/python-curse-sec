from pki_rsa import Pki_rsa
import socket
import threading
import logging


class Client_messenger:
    def __init__(self, host, port):
        self.__HOST = host
        self.__PORT = port
        self.FORMAT = 'utf-8'
        self.user = None
        self.client = None

    def login(self):
        try:
            # Receive Message From Server
            # If 'USER' Send User
            data = self.client.recv(1024).decode(self.FORMAT)
            if data == 'USER':
                self.client.send(self.user.encode(self.FORMAT))
            elif data == 'CORRECT_LOGIN':
                print('CORRECT_LOGIN')
                return True
            else:
                print(data)
        except:
            # Close Connection When Error
            print("An error occured!")
            self.client.close()

    def receive(self):
        data = self.client.recv(1024).decode(self.FORMAT)
        data = data.split("-")

    # Starting Server
    def start(self):
        while True:
            self.user = input("Ingresa Usuario: ")

            print(f"LOGS FILE -> '{self.user}_{self.__HOST}:{self.__PORT}.log'")
            # Create and configure logger
            LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
            logging.basicConfig(filename=f"{self.user}/{self.__HOST}:{self.__PORT}.log", level=logging.DEBUG,
                                format=LOG_FORMAT,
                                filemode='w')
            logger = logging.getLogger()

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client:
                    self.client.connect(self.__HOST, self.__PORT)
                    self.login()

                    # Starting Threads For Receiving
                    receive_thread = threading.Thread(target=self.receive)
                    receive_thread.start()

            except:
                print("Error")
                break


if __name__ == '__main__':
    # Connection Data
    LOCALHOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050  # Port to listen on (non-privileged ports are > 1023)
    my_client = Client_messenger(LOCALHOST, PORT)
    my_client.start()

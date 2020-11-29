import socket
import logging
import time

LOCALHOST = socket.gethostbyname(socket.gethostname())


class Client:
    def __init__(self, host: str, port: str):
        self.__HOST = host
        self.__PORT = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logging.info(f"[CONNECTING TO] {self.__HOST}.")
            s.connect((self.__HOST, self.__PORT))

            for number in range(1, 16):
                message = str(number)
                logging.info(f'Sending: {number}')
                time.sleep(.001)
                s.sendall(message.encode())

            data = s.recv(1024)  # Recibir respuesta
            logging.info(f'Received from server {data.decode()}')

            s.close()
        # s.shutdown(0)


my_client = Client(host=LOCALHOST, port=5050)

my_client.run()

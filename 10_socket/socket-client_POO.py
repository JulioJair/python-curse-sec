import socket
import logging
import time

LOCALHOST = socket.gethostbyname(socket.gethostname())


class Client:
    def __init__(self, host: str, port: str):
        self.__HOST = host
        self.__PORT = port

    def run(self):
        LOG_FORMAT = "%(levelname)s - %(message)s"
        logging.basicConfig(filename=f"{self.__HOST}_client.log", level=logging.DEBUG, format=LOG_FORMAT,
                            filemode='w')
        logger = logging.getLogger()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            logger.info(f"[CONNECTING TO] {self.__HOST}.")
            s.connect((self.__HOST, self.__PORT))

            try:
                for number in range(1, 16):
                    message = str(number)
                    logging.info(f'Sending: {number}')
                    time.sleep(.1)
                    s.sendall(message.encode())

                received = 1
                while received <= 15:
                    data = s.recv(1024)
                    received += 1
                    logger.info(f'Received from server {data.decode()}')
            except:
                logger.error("error sending msg")
            finally:
                logger.info("Closing")
                s.close()





if __name__ == "__main__":
    my_client = Client(host=LOCALHOST, port=5052)
    my_client.run()

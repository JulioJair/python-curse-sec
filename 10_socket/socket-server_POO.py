import socket
import logging
import time

LOCALHOST = socket.gethostbyname(socket.gethostname())


class Server:
    def __init__(self, host: str, port: str):
        self.__HOST = host
        self.__PORT = port
        LOG_FORMAT = "%(levelname)s - %(message)s"
        logging.basicConfig(filename=f"{self.__HOST}_server.log", level=logging.DEBUG, format=LOG_FORMAT,
                            filemode='w')
        self.logger = logging.getLogger()

    def run(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Use the socket object without calling s.close().
            """
            AF_INET is the Internet address family for IPv4.
            SOCK_STREAM is the socket type for TCP
            """

            s.bind((self.__HOST, self.__PORT))
            """
            bind() is used to associate the socket with a specific network interface and port number:
            we’re using socket.AF_INET (IPv4). So it expects a 2-tuple: (host, port)
            """

            s.listen()
            """
            Enables server to accept connection
            """

            self.logger.info(f'[LISTENING] Server is listening on {self.__HOST}')
            conn, addr = s.accept()
            """
            accept() blocks and waits for an incoming connection.
            When a client connects, 
            it returns a new socket object representing the connection (conn) and a tuple (addr).
            The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6. 
            """

            self.listen_client(conn, addr)

    def listen_client(self, conn, addr):
        with conn:
            self.logger.info(f"[NEW CONNECTION] {addr} connected.")
            data = 1
            while True:
                received = 1
                try:
                    while received <= 15:
                        data = conn.recv(1024)  # Receive from client
                        received += 1
                        self.logger.info(f'Received from client {data.decode()}')

                    for number in range(16, 31):
                        message = str(number)
                        logging.info(f'Sending: {number}')
                        time.sleep(.1)
                        conn.sendall(message.encode())
                    break

                except:
                    self.logger.error("Error")
                    self.logger.info("Closing")

                    conn.close()

            self.logger.info("Closing")
            conn.close()

if __name__=="__main__":
    my_server = Server(host=LOCALHOST, port=5052)
    my_server.run()

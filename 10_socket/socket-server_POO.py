import socket
import logging
import time

LOCALHOST = socket.gethostbyname(socket.gethostname())


class Server:
    def __init__(self, host: str, port: str):
        self.__HOST = host
        self.__PORT = port

    def run(self):
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

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

            logging.info(f'[LISTENING] Server is listening on {self.__HOST}')
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
            logging.info(f"[NEW CONNECTION] {addr} connected.")
            while True:
                data = conn.recv(1024)  # Receive from client
                if not data:
                    break
                if data:
                    logging.info(f'Received from client {data.decode()}')
                for number in range(16, 31):
                    message = str(number)
                    logging.info(f'Sending: {number}')
                    time.sleep(.001)
                    conn.sendall(message.encode())

                logging.info('Closing socket')
                conn.shutdown(0)
                conn.close()
                break

                logging.info('Closing socket')
                conn.shutdown(0)
                conn.close()
                break

my_server = Server(host=LOCALHOST, port=5050)

my_server.run()

import socket


class Server:
    def __init__(self, host: str, port: str):
        self.__HOST = host
        self.__PORT = port


    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__HOST, self.__PORT))
            s.listen()
            conn, addr = s.accept()
            self.listen_client(conn, addr)

    def listen_client(self, conn, addr):
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


my_server = Server(host='127.0.0.1', port=40800)

my_server.run()

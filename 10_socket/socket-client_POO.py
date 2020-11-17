<import socket


class Client:
    def __init__(self, host: str, port: str):
        self.__HOST = host
        self.__PORT = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.__HOST, self.__PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)
        print('Received', repr(data))


my_client = Client(host="127.0.0.1", port=40800)

my_client.run()

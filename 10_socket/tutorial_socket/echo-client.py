import socket

LOCALHOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((LOCALHOST, PORT))
    s.sendall(b'1 ')
    s.sendall(b'2 ')
    s.sendall(b'3 ')
    s.sendall(b'4 ')
    s.sendall(b'5 ')
    s.sendall(b'6 ')
    s.sendall(b'7 ')
    s.sendall(b'8 ')
    s.sendall(b'9 ')
    s.sendall(b'10 ')
    s.sendall(b'11 ')
    s.sendall(b'12 ')
    s.sendall(b'13 ')
    s.sendall(b'14 ')
    s.sendall(b'15 ')

    data = s.recv(1024)

print('Received', repr(data))

import socket

LOCALHOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# socket.socket() creates a socket object that supports the context manager type,
# so you can use it in a with statement. There’s no need to call s.close():
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Use the socket object without calling s.close().
    """
    AF_INET is the Internet address family for IPv4.
    SOCK_STREAM is the socket type for TCP
    """
    s.bind((LOCALHOST, PORT))
    """
    bind() is used to associate the socket with a specific network interface and port number:
    we’re using socket.AF_INET (IPv4). So it expects a 2-tuple: (host, port)
    """
    s.listen()
    """
    Enables server to accept connection
    listen() has a backlog parameter. 
    the backlog parameter specifies the number of pending connections the queue will hold.
    Starting in Python 3.5, it’s optional. If not specified, a default backlog value is chosen.
    """
    conn, addr = s.accept()
    """
    accept() blocks and waits for an incoming connection.
    When a client connects, it returns a new socket object representing the connection and a tuple (addr).
    The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6. 
    """
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) #Receive from client
            if not data:
                break
            conn.sendall(data) #Send to client
            conn.sendall(b'16')  # Send to client
            conn.sendall(b'17')
            conn.sendall(b'18')
            conn.sendall(b'19')
            conn.sendall(b'20')
            conn.sendall(b'21')
            conn.sendall(b'22')
            conn.sendall(b'23')
            conn.sendall(b'24')
            conn.sendall(b'25')
            conn.sendall(b'26')
            conn.sendall(b'27')
            conn.sendall(b'28')
            conn.sendall(b'29')
            conn.sendall(b'30')

import socket

LOCALHOST = socket.gethostbyname(socket.gethostname())

HOST = '127.0.0.1'  # La dirección IP del host del socket
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Use the socket object without calling s.close().
    """
    AF_INET is the Internet address family for IPv4.
    SOCK_STREAM is the socket type for TCP
    """
    s.bind((LOCALHOST, PORT))  # Iniciar el socket
    """
                bind() is used to associate the socket with a specific network interface and port number:
                we’re using socket.AF_INET (IPv4). So it expects a 2-tuple: (host, port)
                """
    s.listen()  # Comenzar a escuchar
    conn, addr = s.accept()  # Aceptar peticion de conexión

    with conn:  # Al establecer la conexión
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # Recibir mensaje
            print("Mensaje recibido:", repr(data))
            if not data:  # Si no hay datos, salir
                conn.shutdown(0)
                conn.close()
                break
            conn.sendall(data)  # Responder mensaje

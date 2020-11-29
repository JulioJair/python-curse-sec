import socket

LOCALHOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'  # La dirección IP del host del socket
PORT = 65432  # Puerto utilizado por el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((LOCALHOST, PORT))  # Iniciar el socket
    s.sendall(b'hola mundo')  # Enviar mensaje en formato binario
    data = s.recv(1024)  # Recibir respuesta
    print('Received', repr(data))  # imprimir respuesta
    s.shutdown(0)
    data = s.recv(1024)  # Recibir respuesta
    if data == '':
        s.close()

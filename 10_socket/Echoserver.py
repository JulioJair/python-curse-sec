import socket

HOST = '127.0.0.1'  # La dirección IP del host del socket
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #Iniciar el socket
    s.listen() #Comenzar a escuchar
    conn, addr = s.accept() #Aceptar peticion de conexión
    with conn: #Al establecer la conexión
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) #Recibir mensaje
            print("Mensaje recibido:", repr(data))
            if not data: #Si no hay datos, salir
                conn.shutdown(0)
                conn.close()
                break
            conn.sendall(data) #Responder mensaje
import socket
import threading

FORMAT = 'utf-8'
LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5054
# Choosing User
user = input("Choose your user: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LOCALHOST, PORT))


# Listening to Server and Sending User
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'USER' Send User
            message = client.recv(1024).decode(FORMAT)
            if message == 'USER':
                client.send(user.encode(FORMAT))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        message = input()
        client.send(message.encode(FORMAT))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

import socket
import threading
import logging

FORMAT = 'utf-8'
# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="server.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

# Connection Data
LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5054

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen()
logger.info("[LISTENING]")

# Lists For Clients and Their users
clients = []
users = []
logger.info(f"clients: {clients}")
logger.info(f"clients: {users}")


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)


def send_to(message, index_target):
    clients[index_target].send(message)


# Handling Messages From Clients
def handle(client, index_target):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            send_to(message, index_target)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[index]
            send_to(f'{user} left!'.encode(FORMAT))
            users.remove(user)
            break


def find_user(user,target):
    # Try to find the user
    try:
        index_target = users.index(target)
        print(index_target)

        send_to(f"\n{user} is now talking to you ".encode(FORMAT), index_target)

        return index_target

    except:
        print(f"No se encuentra")
        index_target = 0

        return index_target


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print(f"Connected with {address}")

        # Request And Store user
        client.send('USER'.encode(FORMAT))
        user = client.recv(1024).decode(FORMAT)
        users.append(user)
        clients.append(client)

        # Print And Broadcast user
        print(f"user is {user}")
        client.send('Connected to server!'.encode(FORMAT))
        print(users)
        client.send('Who you want to talk?'.encode(FORMAT))
        target = client.recv(1024).decode(FORMAT)
        # Try to find the user
        index_target = find_user(user,target)

        thread = threading.Thread(target=handle, args=(client, index_target))
        thread.start()


receive()

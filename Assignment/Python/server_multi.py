
import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    data = client_socket.recv(1024).decode()
    print(f"Received from {client_address}: {data}")
    response = f"Message received from {client_address}"
    client_socket.send(response.encode())
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen(10)  # Listen for up to 10 clients
print(f"Server is listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()

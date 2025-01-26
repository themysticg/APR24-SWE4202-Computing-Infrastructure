
import socket

host = '127.0.0.1'
port = 12345

for i in range(10):  # Simulate 10 clients
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = f"Hello from client {i + 1}"
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Client {i + 1} received from server: {response}")
    client_socket.close()

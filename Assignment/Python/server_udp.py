
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
print(f"UDP Server is listening on {host}:{port}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode()}")
    response = f"Message received from {client_address}"
    server_socket.sendto(response.encode(), client_address)

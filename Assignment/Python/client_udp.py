
import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345

# Send data to the server
message = "Hello, UDP Server!"
client_socket.sendto(message.encode(), (host, port))

# Receive a response
data, server_address = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()

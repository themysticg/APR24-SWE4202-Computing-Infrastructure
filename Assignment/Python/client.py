
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # Localhost
port = 12345
client_socket.connect((host, port))

# Send data to the server
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive a response
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close the connection
client_socket.close()

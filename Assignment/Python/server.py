
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
host = '127.0.0.1'  # Localhost
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

# Send a response
response = "Message received by the server!"
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()

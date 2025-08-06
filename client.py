import socket

# Connect to the server
client = socket.socket()
client.connect(('127.0.0.1', 4000))

# Get welcome message
msg = client.recv(1024).decode()
print("From server:", msg)

# Send your message
client.sendall("Hello from the client!".encode())

# Get server's reply
response = client.recv(1024).decode()
print("From server:", response)

# client.close()

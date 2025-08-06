import socket
import threading

# -----------------------------
# Basic server setup
# -----------------------------
HOST = '127.0.0.1'  # This means "localhost" – the current machine
PORT = 4000         # You can use any free port (above 1024 is safe)

# Create a TCP socket (SOCK_STREAM means TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address so it knows where to listen
server.bind((HOST, PORT))

# Start listening for incoming connections (max 5 in queue)
server.listen(5)
print(f"Server is running and listening on {HOST}:{PORT}")

# -----------------------------
# Function to handle a client
# -----------------------------
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    try:
        # Send a message to the client
        welcome_message = "Hey there! You're connected to the server."
        client_socket.sendall(welcome_message.encode())

        # Wait to receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Message from {client_address}: {data}")

        # Optionally, send a response back
        reply = f"Got your message: {data}"
        client_socket.sendall(reply.encode())

    except Exception as error:
        print(f"Error while talking to {client_address}: {error}")

    finally:
        # Always close the connection when done
        client_socket.close()
        print(f"Connection closed with {client_address}")

# -----------------------------
# Main loop to accept clients
# -----------------------------
try:
    while True:
        # Accept new client connections
        client_socket, client_address = server.accept()

        # Handle each client in a new thread (so multiple clients can connect)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

except KeyboardInterrupt:
    print("\nShutting down the server...")
    server.close()

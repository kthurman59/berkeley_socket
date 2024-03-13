import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ("localhost", 8080)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()

    try:
        # Receive data from the client
        data = connection.recv(1024)
        if data:
            # Process the received data
            print("Received:", data)

            # Send a response back to the client
            connection.sendall(b"Message received. Thank you!")
        else:
            break
    finally:
        # Clean up the connection
        connection.close()

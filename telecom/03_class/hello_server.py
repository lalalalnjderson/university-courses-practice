import socket 
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 10000

# 1. create TCP socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. SO_REUSEADDR lets you restart the server immediately after closing it
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 3. bind to an address and port
serverAddress = ('localhost', port)
server.bind(serverAddress)
print(serverAddress)

# 4. start listening for incoming connections, queue at most 1 waiting client
server.listen(1)

# 5. accept a connection (BLOCKS here until a client connects)
connection, clientAddress = server.accept()
print(f"Client connected from {clientAddress}")

# 6. receive data from client 
data = connection.recv(1024).decode()
print(f"received data: {data}")

# 7. send response back 
response = "Hello client"
connection.sendall(response.encode())
print(f"Sent response: {response}")

# 8. close 
connection.close()
server.close()
print("Server shut down.")
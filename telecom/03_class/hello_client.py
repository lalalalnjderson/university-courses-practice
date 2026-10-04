import socket 
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 10000

# 1. create TCP socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect to address (without binding)
serverAddress = ('localhost', port)
client.connect(serverAddress)

# 3. send message to sever 
message = "Hello server"
client.sendall(message.encode())
print(f"client sent: {message}")

# 4. receive response
data = client.recv(1024).decode()
print(f"client received: {data}")

# 5. close
client.close()



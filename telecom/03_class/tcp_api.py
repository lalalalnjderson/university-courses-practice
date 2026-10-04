import socket

# socket() — Create a communication endpoint
# family: AF_INET = IPv4 - as opposed to AF_INET6 for IPv6
# type: SOCK_STREAM (TCP) - as opposed to SOCK_DGRAM for UDP


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)

# localhost - only accept connections from this machine
# '' | '0.0.0.0' - accept from any network interface
# 10000 = port

serverAddress = ('localhost', 10000)
print(serverAddress)

# backlog - how many pending connections to queue up
# listen(1) = queue at most 1 waiting client
# listen(5) = queue up to 5

# accept() — Server blocks, waiting for a client
# Returns: (connection_socket, client_address)

# connect() — Reach out to server (CLIENT only)

sock.close()
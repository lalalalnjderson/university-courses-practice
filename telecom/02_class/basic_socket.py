import socket 

myHostName = socket.gethostname()
print(myHostName)

# resolve a domain name -> ip
try:
    ip = socket.gethostbyname("www.example.org")
    print(ip)
except socket.gaierror as e:
    print(e)

try:
    hostname, aliases, addresses = socket.gethostbyname_ex("www.example.org")
    print(hostname)
    print(aliases)
    print(addresses)
except socket.gaierror as e:
    print(e)

# ip -> hostname
try:
    hostname, aliases, addrs = socket.gethostbyaddr("8.8.8.8")
    print(hostname)
    print(aliases)
    print(addrs)
except socket.herror as e:
    print(e)

# Every network service has a standard port number
wellKnownPorts = [21, 22, 23, 25, 53, 80, 110, 143, 443]
for port in wellKnownPorts:
    try:
        service = socket.getservbyport(port, "tcp")
        print(f"{port} = {service}")
    except  OSError:
        print("unknown service")


testValue = 0x0102
networkShort = socket.htons(testValue)
print(f"0x{networkShort:04x} ({networkShort})")

testLong = 0x01020304
networkLong = socket.htonl(testLong)
print(f"0x{networkLong:08x} ({networkLong})")

backToHost = socket.htons(networkShort)
print(f"0x{backToHost:04x}")



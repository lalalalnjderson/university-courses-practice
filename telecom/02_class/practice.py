import struct
import socket 
import sys

RECORD_FORMAT = '20s i'
packer = struct.Struct(RECORD_FORMAT)

def createSampleFile(filename):
    records = [
        (b'www.example.org', 80),
        (b'google.com', 443),
        (b'localhost', 22),
    ]
    with open(filename, 'wb') as f:
        for domain, port in records:
            paddedDomain = domain.ljust(20, b'\x00')
            f.write(packer.pack(paddedDomain, port))
    for i, (d, p) in enumerate(records):
        print(f"[{i}] domain = {d.decode()}, port = {p}")

def readRecord(filename, lineNumber):
    with open(filename, 'rb') as f:
        f.seek(packer.size * lineNumber)
        data = f.read(packer.size)
        if len(data) < packer.size:
            print(f"Error: record {lineNumber} does not exist")
            sys.exit(1)
        domain, port = packer.unpack(data)
        domain = domain.decode().rstrip('\x00')
        return domain, port

def main():
    binFile = "domains.bin"
    createSampleFile(binFile)
    print()

    if len(sys.argv) == 1:
        print(socket.gethostname())
        return
    
    if len(sys.argv) != 3:
        print("Usage: python practice.py [port|domain] <line>")
        sys.exit(1)

    command = sys.argv[1]
    lineNum = int(sys.argv[2])
    domain, port = readRecord(binFile, lineNum)

    if command == "port":
        try:
            service = socket.getservbyport(port, 'tcp')
            print(f"{port} -> {service}")
        except OSError:
            print("unknown service")

    elif command == "domain":
        try:
            ip = socket.getservbyname(domain)
            print(f"{domain} -> {service}")
        except socket.gaierror as e:
            print(e)

    else:
        print("unknown command")

if __name__ == "__main__":
    main()
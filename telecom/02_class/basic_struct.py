import struct

with open("input.txt", "w") as f:
    f.write("Hello\n")
    f.write("Line 2")

# reads 5 characters
with open("input.txt", "r") as f:
    textData = f.read(5)
    print(textData)
    textData = f.read(8)
    print(textData)

# prints b'Hello' = 'Hello'.encode()
with open("input.txt", "rb") as f:
    binData = f.read(5)
    print(binData) 

# converts python values -> binary bytes
# 2s = string of exactly 2 bytes
values = (1, b'ab', 2.7)
packer = struct.Struct('i 2s f') # define binary structure
packedData = packer.pack(*values) # pack values; * = unpack tuple into separate values
print(packedData)
print(len(packedData)) # bytes
print(packer.size) # expected = 4+2+4 = 10, actual = 12

unpacker = struct.Struct('i 2s f')
unpackedData = unpacker.unpack(packedData)
print(unpackedData)

formats = [
    ('b', 'signed char (1 byte)'),
    ('B', 'unsigned char (1 byte)'),
    ('h', 'short (2 bytes)'),
    ('H', 'unsigned short (2 bytes)'),
    ('i', 'int (4 bytes)'),
    ('I', 'unsigned int (4 bytes)'),
    ('q', 'long long (8 bytes)'),
    ('f', 'float (4 bytes)'),
    ('d', 'double (8 bytes)'),
]

for (fmt, desc) in formats:
    print(f"'{fmt}' = {desc}: calcsize = {struct.calcsize(fmt)}")


# 0x - hexadecimal 
# 4-byte integer: 01 | 02 | 03 | 04 (big -> small)
# in which order to store the bytes?

value = 0x01020304

# native order
nativeBytes = struct.pack('@i', value)
print(nativeBytes.hex())

# little endian order
leBytes = struct.pack('<i', value)
print(leBytes.hex())

# bid endian order
beBytes = struct.pack('>i', value)
print(beBytes.hex())

# network byte order
netBytes = struct.pack('!i', value)
print(netBytes.hex())
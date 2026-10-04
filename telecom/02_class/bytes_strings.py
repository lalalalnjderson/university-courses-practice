import struct

text = "hello"
asBytes = text.encode()
print(text)
print(asBytes)

# 8s - 8-byte string field
# if input is shorter the rest is filled with \x00 (null bytes)
packed = struct.pack('8s', text.encode())
print(packed)

decoded = packed.decode()
print(decoded)

clean = packed.decode().strip('\00')
print(clean)

message = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
toSend = message.encode('utf-8')
print(toSend)

received = b'HTTP/1.1 200 OK\r\n'
asString = received.decode('utf-8')
print(asString.strip())
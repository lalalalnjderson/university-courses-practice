import struct 
import sys

# Task 1
readFormats = [
    '9s i f',
    'f ? c',
    'c i 9s',
    'f 9s ?'
]

for i in range(4):
    packer = struct.Struct(readFormats[i])
    with open(sys.argv[i+1], 'rb') as f:
        data = f.read(packer.size)
        print(packer.unpack(data))

# Task 2
# packed data in (string, tuple) format
packData = [
    ('12s i ?', (b"elso", 52, True)),
    ('f ? c', (55.5, False, b'X')),
    ('i 10s f', (43, b'masodik', 62.9)),
    ('c i 13s', (b'Z', 74, b'harmadik')),
]

for fmt, values in packData:
    print(struct.pack(fmt, *values))

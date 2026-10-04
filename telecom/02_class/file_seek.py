import struct

with open("apple.txt", "w") as f:
    f.write("This is line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open("apple.txt", "r") as f:
    line = f.readline()
    print(line.strip())
    line = f.readline()
    print(line.strip())

    f.seek(0, 0) # return to line 1 again
    line = f.readline()
    print(line.strip())

packer = struct.Struct('i 3s i')
print(packer.size)

with open("dates.bin", "wb") as f:
    for i in range(5):
        values = (2020 + i, b'jan', 10 + i)
        packedData = packer.pack(*values)
        f.write(packedData)

with open("dates.bin", "rb") as f:
    f.seek(packer.size * 3) # skip 3 records (12 * 3)
    data = f.read(packer.size) # f.read(12) so exactly 1 record
    record = packer.unpack(data)
    print(f"with seek: {record[0]}, {record[1].decode()}, {record[2]}")

with open("dates.bin", "rb") as f:
    for i in range(5):
        data = f.read(packer.size)
        record = packer.unpack(data)
        print(f"{record[0]}, {record[1].decode()}, {record[2]}")


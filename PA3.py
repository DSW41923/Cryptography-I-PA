from Crypto.Hash import SHA256

file_bytes = []
with open("6.1.intro.mp4_download", "rb") as f:
    new_byte = f.read(1024)
    while new_byte != "":
        file_bytes.append(new_byte)
        new_byte = f.read(1024)

file_bytes.reverse()
last_hash = b''
for b in file_bytes:
    h = SHA256.new()
    h.update(b + last_hash)
    last_hash = h.digest()

print last_hash.encode('hex')

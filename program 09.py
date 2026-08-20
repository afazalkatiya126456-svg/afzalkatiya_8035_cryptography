import hashlib

text = input("enter message to create hash value:")

sha512_hash = hashlib.sha512(text.encode()).hexdigest()

print("sha-512 hash:",sha512_hash)


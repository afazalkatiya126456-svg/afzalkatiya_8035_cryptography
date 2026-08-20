import hashlib

text = input("enter message to create hash value:")

sha1_hash = hashlib.sha1(text.encode()).hexdigest()

print("sha-1 hash:",sha1_hash)


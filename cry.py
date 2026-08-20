import hashlib

text = input("enter message to create hash value:")

md5_hash = hashlib.md5(text.encode()).hexdigest()

print("md5 hash:",md5_hash)

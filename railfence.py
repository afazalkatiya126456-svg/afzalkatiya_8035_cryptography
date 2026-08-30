from pycipher import Railfence

plaintext=input("enter message: ")
rails=int(input("enter number of rails: "))

cipher=Railfence(rails)

ciphertext=cipher.encipher(plaintext)

print("Encrypted:" , ciphertext)

decrypted= cipher.decipher(ciphertext)

print("decrypted : " , decrypted)

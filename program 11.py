from pycipher import railfence

message = input("enter message:")
rails = int(input("enter number of rails:"))

cipher = railfence(rails)

ciphertext = cipher.encipher(plaintext)

print("encrypted:", ciphertext)

decrypted = cipher.decipher(ciphertext)

print("decrypted:", decrypted)

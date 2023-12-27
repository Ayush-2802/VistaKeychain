from cryptography.fernet import Fernet

#Generating key 
key = Fernet.generate_key()
 
# string the key in a file
with open('keychain.key', 'wb') as filekey:
   filekey.write(key)

with open('keychain.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('Passwords.csv', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)
with open('Passwords.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
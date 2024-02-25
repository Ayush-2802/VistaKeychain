from cryptography.fernet import Fernet

with open('key.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('Passwords.csv', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)
with open('Passwords.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
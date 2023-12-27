from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file
with open('keychain.key', 'wb') as filekey:
    filekey.write(key)
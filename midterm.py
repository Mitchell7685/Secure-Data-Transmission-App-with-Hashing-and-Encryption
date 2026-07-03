import hashlib
from cryptography.fernet import Fernet

# receives the input from the user
message = input("Enter a message: ").encode()

# hashes the original message for integrity check
original_hash = hashlib.sha256(message).hexdigest()
print("\nSHA-256 hash:", original_hash)

# Encrypts the message
key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(message)
print("Encrypted:", encrypted)


# Decrypts the message
decrypted = f.decrypt(encrypted)
print("Decrypted:", decrypted.decode())


# Checkes the integrity of the message
new_hash= hashlib.sha256(decrypted).hexdigest()
print("\nNew hash: ", new_hash)

if new_hash == original_hash:
    print("Integrity is okay, message matches")
else:
    print("Integrity failed, massage changed")

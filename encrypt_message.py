from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Step 1: Generate a key and IV (32 bytes for AES-256)
key = get_random_bytes(32)  # AES-256 key length (32 bytes)
iv = get_random_bytes(16)   # AES block size (16 bytes)

print("Key:", base64.b64encode(key).decode('utf-8'))
print("IV:", base64.b64encode(iv).decode('utf-8'))

# Step 2: Define a function to pad the data to be encrypted
def pad(data):
    padding_len = AES.block_size - len(data) % AES.block_size
    padding = bytes([padding_len] * padding_len)
    return data + padding

# Step 3: Encrypt data
def encrypt(plain_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plain_text.encode('utf-8'))
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Step 4: Define a function to unpad the decrypted data
def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

# Step 5: Decrypt data
def decrypt(encrypted_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_text)
    return unpad(decrypted_data).decode('utf-8')

# Test the functions
plain_text = "YOUR-MESSAGE"
print("Original:", plain_text)

encrypted_data = encrypt(plain_text, key, iv)
print("Encrypted (base64):", base64.b64encode(encrypted_data).decode('utf-8'))

# Write the encrypted data to a file in binary mode
with open('encrypted.bin', 'wb') as file:
    file.write(encrypted_data)

# Read the encrypted data from the file and decrypt it
with open('encrypted.bin', 'rb') as file:
    encrypted_data_from_file = file.read()

decrypted_text = decrypt(encrypted_data_from_file, key, iv)
print("Decrypted:", decrypted_text)

input("Press enter to exit.")

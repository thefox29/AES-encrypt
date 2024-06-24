from Crypto.Cipher import AES
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('key-iv.env')  # Specify the correct path to your .env file

# Retrieve the key and IV from environment variables
key_b64 = os.getenv('ENCRYPTION_KEY')
iv_b64 = os.getenv('ENCRYPTION_IV')

# Ensure both variables are not None
if key_b64 is None or iv_b64 is None:
    raise ValueError("Encryption key or IV not found in environment variables")

# Decode the base64 encoded key and IV
key = base64.b64decode(key_b64)
iv = base64.b64decode(iv_b64)

# Define a function to unpad the decrypted data
def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

# Step 1: Read the encrypted data from the file
with open('encrypted.bin', 'rb') as file:
    encrypted_data = file.read()

# Step 2: Decrypt the data
def decrypt(encrypted_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_text)
    return unpad(decrypted_data)

# Decrypt the data read from the file
decrypted_text = decrypt(encrypted_data, key, iv).decode('utf-8')
print("Decrypted:", decrypted_text)

input("Press Enter to exit...")

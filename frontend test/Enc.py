import os
from cryptography.fernet import Fernet

# Generate and save the key
def generate_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)

# Load the encryption key
def load_key():
    return open('key.key', 'rb').read()

# Encrypt a file
def encrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Main function to encrypt files
def main():
    generate_key()
    key = load_key()
    fernet = Fernet(key)
    
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file not in ['encrypt.py', 'decrypt.py', 'key.key']:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, fernet)
                print(f'Encrypted {file_path}')

if __name__ == "__main__":
    main()

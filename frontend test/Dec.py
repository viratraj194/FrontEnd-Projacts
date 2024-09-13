import os
from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    return open('key.key', 'rb').read()

# Decrypt a file
def decrypt_file(file_path, fernet):
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Main function to decrypt files
def main():
    key = load_key()
    fernet = Fernet(key)
    
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file not in ['encrypt.py', 'decrypt.py', 'key.key']:
                file_path = os.path.join(root, file)
                decrypt_file(file_path, fernet)
                print(f'Decrypted {file_path}')

if __name__ == "__main__":
    main()
  

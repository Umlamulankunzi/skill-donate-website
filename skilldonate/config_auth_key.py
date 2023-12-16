import json
from cryptography.fernet import Fernet
from decouple import config




def init():
    # Load encryption key
    key = config('ENKEY')

    # Initialize Fernet
    fk = Fernet(key)

    # Load and decrypt credentials
    with open('encrypted_credentials', 'rb') as f:
        encrypted = f.read()
        decrypted = fk.decrypt(encrypted).decode()

    # Use decrypted credentials
    with open('creds.json', 'w+') as f:
        json.dump(json.loads(decrypted), f)

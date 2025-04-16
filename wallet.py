# wallet.py

from solders.keypair import Keypair

import base58

def load_keypairs_from_file(filepath):
    keypairs = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            secret_key = base58.b58decode(line)
            keypair = Keypair.from_secret_key(secret_key)
            keypairs.append(keypair)
    return keypairs

# spl_token_utils.py

from solders.pubkey import Pubkey
from spl.token.instructions import get_associated_token_address, create_associated_token_account, transfer_checked
from solana.transaction import Transaction

def get_or_create_ata(client, payer, owner_pubkey, mint_pubkey):
    ata = get_associated_token_address(owner_pubkey, mint_pubkey)
    resp = client.get_account_info(ata)
    if resp['result']['value'] is None:
        tx = Transaction()
        tx.add(create_associated_token_account(payer.public_key, owner_pubkey, mint_pubkey))
        client.send_transaction(tx, payer)
    return ata

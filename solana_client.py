# solana_client.py

from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.rpc.commitment import Confirmed


class SolanaClient:
    def __init__(self, rpc_endpoint):
        self.client = Client(rpc_endpoint)

    def send_transaction(self, transaction: Transaction, signer):
        resp = self.client.send_transaction(transaction, signer)
        signature = resp.get('result')
        if not signature:
            raise Exception(f"Transaction failed: {resp}")
        self.client.confirm_transaction(signature, commitment=Confirmed)
        return signature

    def get_token_balance(self, token_account_pubkey):
        return self.client.get_token_account_balance(token_account_pubkey)

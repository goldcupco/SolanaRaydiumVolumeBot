# main.py

from solana.rpc.api import Client
from solders.pubkey import Pubkey
from solders.keypair import Keypair


from settings import (
    RPC,
    TOKEN_ADDRESS,
    SLIPPAGE,
    SOL_IN,
    SELL_PERCENTAGE_MIN,
    SELL_PERCENTAGE_MAX,
    SELL_PROBABILITY,
    CYCLES,
    DELAY_BETWEEN_ROUNDS,
    PRIVATE_KEYS_FILE,
    THREADS,
)
from bot import SolanaRaydiumVolumeBot

def main():
    bot = SolanaRaydiumVolumeBot(
        rpc_endpoint=RPC,
        token_address=TOKEN_ADDRESS,
        slippage=SLIPPAGE,
        sol_in=SOL_IN,
        sell_percentage_min=SELL_PERCENTAGE_MIN,
        sell_percentage_max=SELL_PERCENTAGE_MAX,
        sell_probability=SELL_PROBABILITY,
        cycles=CYCLES,
        delay_between_rounds=DELAY_BETWEEN_ROUNDS,
        private_keys_file=PRIVATE_KEYS_FILE,
        threads=THREADS,
    )
    bot.run()

if __name__ == "__main__":
    main()

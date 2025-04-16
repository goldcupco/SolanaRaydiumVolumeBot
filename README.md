# Solana Raydium AMM Volume Bot

This project is an asynchronous, multi-threaded bot for trading tokens on the Solana blockchain. It performs a buy operation on a specified token for multiple wallets (loaded from a file) and may perform a sell operation based on a configurable probability and random sale percentage within a given range.

## Features

- **Multi-Wallet Support:** Reads private keys from `private_keys.txt` (one key per line) to operate on multiple wallets.
- **Asynchronous & Concurrent Execution:** Uses `asyncio` with a configurable semaphore to simulate multi-threading.
- **Configurable Trade Settings:** All trade parameters (RPC endpoint, token address, SOL amount, slippage, sell probability, sale percentage range, trade cycles, etc.) are set in `settings.py`.
- **Randomized Sell Percentage:** When a sell operation is triggered, the percentage of tokens to sell is chosen randomly within a configurable range.



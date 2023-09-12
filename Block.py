import hashlib
import json
from time import time


class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time()
        self.transactions = transactions
        self.nonce = 0  # For Proof-of-Work
        self.merkle_root = self.calculate_merkle_root()

    def calculate_merkle_root(self):
        # Simplified example; in a real-world application,
        # you would use a Merkle tree structure for efficiency
        transaction_hashes = [hashlib.sha256(json.dumps(tx).encode()).hexdigest() for tx in self.transactions]
        return hashlib.sha256("".join(transaction_hashes).encode()).hexdigest()

    def hash_block(self):
        block_string = json.dumps({
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'merkle_root': self.merkle_root,
            'nonce': self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()
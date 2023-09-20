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
        self.merkle_root = merkle_tree_root(transactions)

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

def merkle_tree_root(transactions):
    if not transactions:
        return ''

    tx_hashes = [hashlib.sha256(json.dumps(tx).encode()).hexdigest() for tx in transactions]

    while len(tx_hashes) > 1:
        if len(tx_hashes) % 2 != 0:
            tx_hashes.append(tx_hashes[-1])

        new_level = []

        for i in range(0, len(tx_hashes), 2):
            new_hash = hashlib.sha256((tx_hashes[i] + tx_hashes[i + 1]).encode()).hexdigest()
            new_level.append(new_hash)

        tx_hashes = new_level

    return tx_hashes[0]
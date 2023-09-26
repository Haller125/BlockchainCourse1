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
    
    def proof_of_work(self, difficulty):
        # Find a number nonce such that hash of the block with nonce has `difficulty` leading zeros
        while self.hash_block()[:difficulty] != '0' * difficulty:
            self.nonce += 1

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
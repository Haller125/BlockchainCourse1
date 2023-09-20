from Block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.mempool = []
        self.initialize_genesis_block()

    def initialize_genesis_block(self):
        genesis_block = Block(
            index=0,
            previous_hash="0",
            transactions=[]
        )
        self.add_block(genesis_block)

    def add_block(self, block):
        block_hash = block.hash_block()
        self.chain.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'transactions': block.transactions,
            'nonce': block.nonce,
            'merkle_root': block.merkle_root,
            'previous_hash': block.previous_hash,
            'hash': block_hash
        })

    def add_new_block(self, transactions):
        last_block = self.chain[-1]
        index = last_block['index'] + 1
        previous_hash = last_block['hash']
        new_block = Block(
            index=index,
            previous_hash=previous_hash,
            transactions=transactions
        )
        # Here you might include a Proof-of-Work or other consensus algorithm
        self.add_block(new_block)

    def add_transaction_to_mempool(self, transaction):
        # In real-world, you'll verify the transaction first.
        # For example, check if the sender has enough balance.
        self.mempool.append(transaction)

    def mine_block(self):
        if not self.mempool:
            print("No transactions to mine.")
            return

        last_block = self.chain[-1]
        index = last_block['index'] + 1
        previous_hash = last_block['hash']

        new_block = Block(
            index=index,
            previous_hash=previous_hash,
            transactions=self.mempool
        )

        # Here you might include a Proof-of-Work or other consensus algorithm
        self.add_block(new_block)

        # Clear the mempool
        self.mempool = []
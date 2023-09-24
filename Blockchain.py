from Block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.mempool = []
        self.balances = {}
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

    def add_new_block(self, transactions, difficulty=4):
        last_block = self.chain[-1]
        index = last_block['index'] + 1
        previous_hash = last_block['hash']
        new_block = Block(
            index=index,
            previous_hash=previous_hash,
            transactions=transactions
        )

        # Here you might include a Proof-of-Work or other consensus algorithm --Here we go: 
        new_block.proof_of_work(difficulty)

        self.add_block(new_block)

    def add_transaction_to_mempool(self, transaction):
        sender = transaction['sender']
        recipient = transaction['recipient']
        amount = transaction['amount']

        # Initialize sender and recipient in balances if they don't exist
        if sender not in self.balances:
            self.balances[sender] = 100  # giving an initial amount of 100 for this example
        if recipient not in self.balances:
            self.balances[recipient] = 100  # giving an initial amount of 100 for this example

        # Check if the sender has enough balance
        if self.balances[sender] < amount:
            print(f"Transaction failed! {sender} has insufficient funds.")
            return

        # Check for negative transactions
        if amount <= 0:
            print("Transaction failed! Amount should be positive.")
            return

        # If all checks pass, add transaction to mempool
        self.mempool.append(transaction)

    def mine_block(self, difficulty=4):
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

        # Here you might include a Proof-of-Work or other consensus algorithm --Here we go:
        new_block.proof_of_work(difficulty)

        self.add_block(new_block)

        # Update balances based on the transactions in the mined block
        for tx in new_block.transactions:
            sender = tx['sender']
            recipient = tx['recipient']
            amount = tx['amount']
            
            # Deduct from sender's balance
            if sender in self.balances:
                self.balances[sender] -= amount
            else:
                self.balances[sender] = -amount
            
            # Add to recipient's balance
            if recipient in self.balances:
                self.balances[recipient] += amount
            else:
                self.balances[recipient] = amount

        # Clear the mempool after mining
        self.mempool = []

    def validate_chain(self):
        # Start from the second block and compare with its previous
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the previous_hash matches the hash of the previous block
            if current_block['previous_hash'] != previous_block['hash']:
                return False

            # Validate block's own hash
            reconstructed_block = Block(
                index=current_block['index'],
                previous_hash=current_block['previous_hash'],
                transactions=current_block['transactions'],
                timestamp=current_block['timestamp']
            )
            reconstructed_block.nonce = current_block['nonce']
            if reconstructed_block.hash_block() != current_block['hash']:
                return False

        return True

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
        # In real-world, you'll verify the transaction first.
        # For example, check if the sender has enough balance.
        sender = transaction['sender']
        recipient = transaction['recipient']
        amount = transaction['amount']
    
        # Check if the sender has enough balance
        if sender not in self.balances:
            self.balances[sender] = 0
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
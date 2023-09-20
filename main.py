from Blockchain import Blockchain

blockchain = Blockchain()

print("Genesis Block:", blockchain.chain[0])

blockchain.add_new_block(transactions=[{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}])
blockchain.add_new_block(transactions=[{'sender': 'Bob', 'recipient': 'Charlie', 'amount': 30}])

blockchain.mine_block()

for block in blockchain.chain:
    print("Block:", block)
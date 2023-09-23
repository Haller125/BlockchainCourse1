from Blockchain import Blockchain

blockchain = Blockchain()

# print("Genesis Block:", blockchain.chain[0])

# blockchain.add_new_block(transactions=[{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}])
# blockchain.add_new_block(transactions=[{'sender': 'Bob', 'recipient': 'Charlie', 'amount': 30}])

# blockchain.mine_block()

# for block in blockchain.chain:
#     print("Block:", block)

def display_blockchain(blockchain):
    for block in blockchain.chain:
        print("\nBlock:", block)
        print("-------------")

def add_transaction(blockchain):
    sender = input("Enter sender: ")
    recipient = input("Enter recipient: ")
    amount = float(input("Enter amount: "))  # assuming the amount is float for simplicity
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    blockchain.add_transaction_to_mempool(transaction)
    print("Transaction added to mempool!")

def mine_block(blockchain):
    blockchain.mine_block()
    print("Block mined successfully!")

def main():
    blockchain = Blockchain()
    while True:
        print("\nBlockchain Console Interface:")
        print("1. Display Blockchain")
        print("2. Add Transaction to Mempool")
        print("3. Mine Block")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_blockchain(blockchain)
        elif choice == "2":
            add_transaction(blockchain)
        elif choice == "3":
            mine_block(blockchain)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

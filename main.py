from Blockchain import Blockchain

# blockchain = Blockchain()

# print("Genesis Block:", blockchain.chain[0])

def display_block(block):
    print("\n--------------------- Block ---------------------")
    for key, value in block.items():
        if key == "transactions" and value:
            print("\nTransactions:")
            for tx in value:
                print(f"   Sender: {tx['sender']} -> Recipient: {tx['recipient']} Amount: {tx['amount']}")
        else:
            print(f"{key.capitalize():15}: {value}")
    print("--------------------------------------------------")

def display_blockchain(blockchain):
    for block in blockchain.chain:
        display_block(block)

def add_transaction(blockchain):
    try:
        sender = input("Enter sender: ")
        recipient = input("Enter recipient: ")
        amount = float(input("Enter amount: "))  # Assuming the amount is float for simplicity
        if amount <= 0:
            print("Please enter a valid positive amount.")
            return
        transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
        blockchain.add_transaction_to_mempool(transaction)
        print("Transaction added to mempool!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value for the transaction amount.")

def mine_block(blockchain):
    blockchain.mine_block()
    print("Block mined successfully!")

def view_balances(blockchain):
    for user, balance in blockchain.balances.items():
        print(f"{user}: {balance} coins")

def main():
    blockchain = Blockchain()
    while True:
        print("\nBlockchain Console Interface:")
        print("1. Display Blockchain")
        print("2. Add Transaction to Mempool")
        print("3. Mine Block")
        print("4. View Balances")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                display_blockchain(blockchain)
            elif choice == "2":
                add_transaction(blockchain)
            elif choice == "3":
                mine_block(blockchain)
            elif choice == "4":
                view_balances(blockchain)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
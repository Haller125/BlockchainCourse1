# Blockchain Course Assignment

## Overview
This assignment provides a simplified implementation of a blockchain, complete with blocks, transactions, a mempool, and a basic proof-of-work consensus algorithm.

### Files
1. `tests/test_blockchain.py`: Contains unit tests for the blockchain.
2. `Block.py`: Defines the `Block` class, responsible for creating individual blocks and their associated operations.
3. `Blockchain.py`: Contains the `Blockchain` class, which is responsible for overall chain operations such as adding blocks and transactions to the mempool.
4. `main.py`: The main driver code for a console interface, where you can interact with the blockchain, add transactions, mine blocks, etc.

## How to Run

1. **Run the tests**:
   ```
   python3 -m unittest discover -s tests
   ```

2. **Run the blockchain console**:
   ```
   python3 main.py
   ```

## Brief File Explanation

### `tests/test_blockchain.py`
- **TestBlock**: Contains unit tests for the `Block` class.
    - `test_merkle_tree_root()`: Tests the Merkle tree root function.
    - `test_hash_block()`: Tests the block's hashing mechanism.
  
- **TestBlockchain**: Contains unit tests for the `Blockchain` class.
    - `test_initialize_genesis_block()`: Tests the initialization of the genesis block.
    - `test_add_new_block()`: Tests the addition of a new block to the chain.
    - `test_add_transaction_to_mempool()`: Tests the addition of a transaction to the mempool.
    - `test_mine_block()`: Tests the block mining operation.

### `Block.py`
- **Block**: Represents an individual block in the blockchain.
    - Contains methods related to calculating the Merkle root, hashing a block, and a basic proof-of-work mechanism.

- **merkle_tree_root(transactions)**: A function to generate the Merkle tree root for a given set of transactions.

### `Blockchain.py`
- **Blockchain**: Represents the blockchain.
    - Handles operations like adding blocks, managing transactions in the mempool, and keeping track of user balances.

### `main.py`
- Console interface to interact with the blockchain.
    - Options to display the blockchain, add transactions to the mempool, mine blocks, view user balances, and exit.

## Usage Guidelines:

- When adding a transaction, the sender and recipient are initialized with a balance of 100 coins (if they don't already exist).
- The mining operation includes a basic proof-of-work mechanism, looking for a nonce such that the hash of the block starts with a specific number of leading zeros (default difficulty is set to 4).
- Successful transactions are added to the mempool and get included in the next mined block.
- After mining a block, transactions in the block are used to update user balances.

**Note**: This is a simplified representation of a blockchain, meant for educational purposes. It does not include all the security features and optimizations of a real-world blockchain.

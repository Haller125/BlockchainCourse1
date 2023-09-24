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

### Blockchain principles

1. Distributed Ledger
A blockchain is a type of distributed ledger, which means that a single, identical copy of the record is stored across multiple nodes or computers in a network. No single entity controls the blockchain, making it decentralized. This helps to enhance security and fault tolerance.
2. Consensus Mechanism
The network must agree on the validity of transactions to maintain integrity. Various consensus algorithms like Proof-of-Work (PoW), Proof-of-Stake (PoS), and Practical Byzantine Fault Tolerance (PBFT) are used to achieve this.
3. Immutability
Once a block is added to the blockchain, it cannot be altered or removed. This ensures that past records are secure and tamper-evident. Immutability is often secured by cryptographic hash functions.
4. Transparency
Every transaction on the blockchain is transparent and verifiable by all users of the network. While identities might be pseudonymous, the transaction history of every blockchain address is publicly viewable by anyone.
5. Smart Contracts (optional for your assignment)
Though not required for your assignment, smart contracts are self-executing contracts where the contract terms are directly written into code. They run on the blockchain, which means they are decentralized and can run without the need for intermediaries.
6. Merkle Trees
In the context of blockchains, Merkle trees help in efficiently summarizing all the transactions in a block, thereby ensuring that data can be easily verified. They play a vital role in optimizing and verifying the large sets of data stored in blocks.
7. Blocks and Chain
Blocks are essentially batches of verified transactions that are "chained" together in a linear, chronological order. Each block contains a reference to the previous block via its hash, thereby forming a chain. This interconnectedness ensures that the entire transaction history can be traced back to the so-called "Genesis Block."
8. Cryptographic Hash Functions
Blockchain employs cryptographic hash functions (typically SHA-256 in Bitcoin) for various purposes such as generating addresses, forming the identification of blocks, and creating digital signatures for transaction authentication.
9. Peer-to-Peer Network
Blockchain operates on a peer-to-peer (P2P) network architecture. Nodes in these networks are equal participants that can serve both as clients and servers, enhancing redundancy and resiliency.
10. Transparency vs Privacy
There's a delicate balance to be maintained between transparency and privacy. While all transactions are transparent and verifiable, blockchain provides a level of privacy by not disclosing the identities associated with blockchain addresses unless that information is revealed during a transaction.


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

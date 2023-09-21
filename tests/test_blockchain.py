import unittest
from Block import Block, merkle_tree_root
from Blockchain import Blockchain

class TestBlock(unittest.TestCase):
    
    def test_merkle_tree_root(self):
        transactions = [{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}]
        self.assertIsInstance(merkle_tree_root(transactions), str)
        self.assertNotEqual(merkle_tree_root(transactions), '')
        
    def test_hash_block(self):
        block = Block(0, '0', [])
        self.assertIsInstance(block.hash_block(), str)
        self.assertNotEqual(block.hash_block(), '')

class TestBlockchain(unittest.TestCase):
    
    def setUp(self):
        self.blockchain = Blockchain()
        
    def test_initialize_genesis_block(self):
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0]['index'], 0)
        self.assertEqual(self.blockchain.chain[0]['previous_hash'], '0')

    def test_add_new_block(self):
        self.blockchain.add_new_block([{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}])
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(self.blockchain.chain[1]['index'], 1)

    def test_add_transaction_to_mempool(self):
        self.blockchain.add_transaction_to_mempool({'sender': 'Alice', 'recipient': 'Bob', 'amount': 50})
        self.assertEqual(len(self.blockchain.mempool), 1)
    
    def test_mine_block(self):
        self.blockchain.add_transaction_to_mempool({'sender': 'Alice', 'recipient': 'Bob', 'amount': 50})
        self.blockchain.mine_block()
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(len(self.blockchain.mempool), 0)
        
if __name__ == '__main__':
    unittest.main()

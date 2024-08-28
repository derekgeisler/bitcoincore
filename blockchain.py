# blockchain.py
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def add_block(self, block):
        if self.validate_block(block):
            self.chain.append(block)

    def validate_block(self, block):
        # Implement block validation logic here
        return True

    def latest_block(self):
        return self.chain[-1] if self.chain else None

    def create_genesis_block(self):
        genesis_block = {
            'index': 0,
            'previous_hash': '0',
            'timestamp': 1231006505,  # Bitcoin's genesis block timestamp
            'transactions': [],
            'hash': self.hash_block('genesis')
        }
        self.chain.append(genesis_block)

    def hash_block(self, block):
        # Implement a function to hash a block
        return 'blockhash'

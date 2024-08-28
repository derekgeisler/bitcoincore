# transaction.py
import hashlib

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.tx_hash = self.compute_hash()

    def compute_hash(self):
        tx_contents = f"{self.sender}{self.recipient}{self.amount}"
        return hashlib.sha256(tx_contents.encode('utf-8')).hexdigest()

    def sign_transaction(self, private_key):
        signature = private_key.sign(self.tx_hash.encode('utf-8'))
        return signature

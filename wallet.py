# wallet.py
import ecdsa
import hashlib

class Wallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()

    def generate_private_key(self):
        return ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    def generate_public_key(self):
        return self.private_key.get_verifying_key()

    def sign_transaction(self, transaction):
        return self.private_key.sign(transaction.encode('utf-8'))

    def get_address(self):
        public_key_bytes = self.public_key.to_string()
        sha256_bpk = hashlib.sha256(public_key_bytes).digest()
        ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
        return ripemd160_bpk

# Example usage
if __name__ == "__main__":
    wallet = Wallet()
    print(f"Public Address: {wallet.get_address().hex()}")

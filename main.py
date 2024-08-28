# main.py
from networking import BitcoinNode
from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction

def main():
    blockchain = Blockchain()
    blockchain.create_genesis_block()

    wallet = Wallet()
    print(f"Your Bitcoin address: {wallet.get_address().hex()}")

    node = BitcoinNode()
    node.connect()

    # Example of creating a transaction
    tx = Transaction(wallet.get_address(), 'recipient_address', 1.0)
    signature = wallet.sign_transaction(tx.tx_hash)
    print(f"Transaction Hash: {tx.tx_hash}")
    print(f"Signature: {signature.hex()}")

    node.close()

if __name__ == "__main__":
    main()

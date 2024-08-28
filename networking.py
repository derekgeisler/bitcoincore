# networking.py
import socket

class BitcoinNode:
    def __init__(self, host='localhost', port=8333):
        self.host = host
        self.port = port

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")

    def send(self, message):
        self.sock.sendall(message)

    def receive(self):
        response = self.sock.recv(4096)
        return response

    def close(self):
        self.sock.close()

# Example usage
if __name__ == "__main__":
    node = BitcoinNode('127.0.0.1', 8333)
    node.connect()
    # Send/receive messages according to the Bitcoin protocol
    node.close()

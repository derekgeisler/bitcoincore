# utils.py
import hashlib
import ecdsa
import base58

def sha256(data):
    """Return the SHA-256 hash of the given data."""
    return hashlib.sha256(data).digest()

def ripemd160(data):
    """Return the RIPEMD-160 hash of the given data."""
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(data)
    return ripemd160.digest()

def double_sha256(data):
    """Perform a double SHA-256 hash."""
    return sha256(sha256(data))

def hash160(data):
    """Perform a SHA-256 followed by a RIPEMD-160."""
    return ripemd160(sha256(data))

def generate_private_key():
    """Generate a new private key."""
    return ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

def private_key_to_public_key(private_key):
    """Convert a private key to a public key."""
    return private_key.get_verifying_key().to_string()

def public_key_to_address(public_key):
    """Convert a public key to a Bitcoin address."""
    # Perform SHA-256 followed by RIPEMD-160 (hash160)
    pubkey_hash = hash160(public_key)

    # Add version byte (0x00 for mainnet)
    versioned_pubkey_hash = b'\x00' + pubkey_hash

    # Perform double SHA-256 for checksum
    checksum = double_sha256(versioned_pubkey_hash)[:4]

    # Combine the versioned hash with the checksum
    binary_address = versioned_pubkey_hash + checksum

    # Encode in Base58
    address = base58.b58encode(binary_address)

    return address.decode()

def wif_to_private_key(wif):
    """Convert a WIF (Wallet Import Format) string to a private key."""
    # Decode WIF from Base58
    decoded = base58.b58decode(wif)

    # Drop the first byte (0x80 for mainnet) and the last 4 checksum bytes
    private_key = decoded[1:-4]

    return private_key

def private_key_to_wif(private_key):
    """Convert a private key to WIF (Wallet Import Format)."""
    # Add version byte (0x80 for mainnet)
    versioned_key = b'\x80' + private_key

    # Perform double SHA-256 for checksum
    checksum = double_sha256(versioned_key)[:4]

    # Combine the versioned key with the checksum
    binary_wif = versioned_key + checksum

    # Encode in Base58
    wif = base58.b58encode(binary_wif)

    return wif.decode()

def sign_message(private_key, message):
    """Sign a message with a private key."""
    return private_key.sign(message.encode('utf-8'))

def verify_signature(public_key, message, signature):
    """Verify a signature with the corresponding public key."""
    return public_key.verify(signature, message.encode('utf-8'))

def encode_varint(i):
    """Encode an integer as a variable length integer (varint)."""
    if i < 0xfd:
        return i.to_bytes(1, 'little')
    elif i <= 0xffff:
        return b'\xfd' + i.to_bytes(2, 'little')
    elif i <= 0xffffffff:
        return b'\xfe' + i.to_bytes(4, 'little')
    else:
        return b'\xff' + i.to_bytes(8, 'little')

def decode_varint(data):
    """Decode a variable length integer (varint) from data."""
    if data[0] < 0xfd:
        return data[0], 1
    elif data[0] == 0xfd:
        return int.from_bytes(data[1:3], 'little'), 3
    elif data[0] == 0xfe:
        return int.from_bytes(data[1:5], 'little'), 5
    else:
        return int.from_bytes(data[1:9], 'little'), 9

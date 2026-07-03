# Secure Data Transmission App

A Python application that demonstrates secure data transmission using hashing and encryption techniques.

## Overview

This application demonstrates fundamental cybersecurity concepts by:

- **Hashing**: Uses SHA-256 to create a hash of the original message for integrity verification
- **Encryption**: Encrypts messages using Fernet (symmetric encryption) from the cryptography library
- **Integrity Checking**: Verifies that encrypted and decrypted messages maintain their integrity by comparing hashes

## Features

- User input for custom messages
- SHA-256 hashing for message integrity
- Fernet symmetric encryption/decryption
- Automated integrity verification

## Requirements

- Python 3.6+
- cryptography library

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python midterm.py
```

Then enter a message when prompted. The application will display:

- The SHA-256 hash of the original message
- The encrypted message
- The decrypted message
- A new hash of the decrypted message
- Confirmation of message integrity

Confidentiality is upheld through AES-based Fernet encryption. Once the message is encrypted, it's unreadable to anyone without the secret key using the cipher. Even if the encrypted output is intercepted, the original content stays hidden.

Integrity is upheld through the SHA-256 hash. Hashing the message before encryption creates a fixed-length fingerprint of the original data. After decryption, it re-hashes the result and compares it to the original hash. If any part of the message changed in transit or storage, the two hashes would not match, immediately flagging tampering or corruption.

Availability is supported by keeping itself self-contained. The key and encrypted message are generated and used within the same run, so there's no dependency on external servers or services that could go down.

Fernet.generate_key() creates a random 256-bit key using Python's cryptographically secure random number generator. Entropy is what keeps the key difficult to guess. Using Fernet ensures high entropy. A key generated with low entropy would be vulnerable to brute-force or dictionary attacks. Because Fernet pulls from a secure source of randomness, the resulting key is statistically unpredictable, which is what gives the encryption its strength. 

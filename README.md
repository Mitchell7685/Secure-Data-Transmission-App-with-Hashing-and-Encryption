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


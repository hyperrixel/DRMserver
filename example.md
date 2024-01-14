# Video Encryption and Decryption User Documentation

This document provides detailed instructions on how to use the provided Python script for video encryption and decryption. Before proceeding, please read through the following guidelines.

## Table of Contents
- [Video Encryption and Decryption User Documentation](#video-encryption-and-decryption-user-documentation)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [How to Install Prerequisites](#how-to-install-prerequisites)
    - [OpenCV](#opencv)
    - [NumPy](#numpy)
    - [DRMserver](#drmserver)
  - [Usage](#usage)
    - [Decoding (Decrypting) a Video](#decoding-decrypting-a-video)
    - [Encoding (Encrypting) a Video](#encoding-encrypting-a-video)
    - [Warnings and Notifications](#warnings-and-notifications)

## Prerequisites

Before using the script, make sure you have the necessary dependencies installed:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- Custom Cryptographer class (`drm_server.cryptographer.Cryptographer`)

## How to Install Prerequisites

### OpenCV

To install OpenCV (Open Source Computer Vision Library) using the `pip` package manager, follow these steps:

1. Open your command-line terminal or command prompt.

2. Run the following command to install OpenCV:

```bash
pip install opencv-python
```

### NumPy

To install NumPy using the `pip` package manager, follow these steps:

1. Open your command-line terminal or command prompt.

2. Run the following command to install NumPy:

```bash
pip install numpy
```

### DRMserver

To clone the **DRMserver** repository from a Git repository and unpack the contents, follow these steps:

1. Open your command-line terminal or command prompt.

2. Run the following command to clone the DRMserver repository:

```bash
git clone https://github.com/hyperrixel/DRMserver/repository.git
```

## Usage

### Decoding (Decrypting) a Video

To decrypt a video file, use the `decode` function. Provide the input and output file paths and, optionally, a custom decoder.

```python
from drm_server.cryptographer import Cryptographer

# Example usage:
key = b'YOUR_TEST_KEY'
nonce = b'YOUR_TEST_NONCE'
cryptographer = Cryptographer('AES', 256, 'CTR', 128, True, key, nonce)
decode('SOURCE_PATH', 'DESTINATION_PATH', cryptographer)
```

### Encoding (Encrypting) a Video

To encrypt a video file, use the encode function. Provide the input and output file paths and, optionally, a custom encoder.

```python
from drm_server.cryptographer import Cryptographer

# Example usage:
key = b'YOUR_TEST_KEY'
nonce = b'YOUR_TEST_NONCE'
cryptographer = Cryptographer('AES', 256, 'CTR', 128, True, key, nonce)
encode('SOURCE_PATH', 'DESTINATION_PATH', cryptographer)
```

### Warnings and Notifications

- Ensure all dependencies are installed before running the script.
- Provide valid file paths for input and output video files.
- The provided Cryptographer class should be correctly implemented and accessible.
- The key and nonce values in the examples are placeholders; replace them with your actual encryption key and nonce.

Important Note: This script is intended for educational and experimental purposes. Ensure compliance with legal and ethical standards when using video encryption techniques.


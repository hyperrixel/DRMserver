# Cryptographer Class

The `Cryptographer` class is designed to handle cryptographic operations using the Advanced Encryption Standard (AES) algorithm in Cipher Block Chaining (CBC) or Counter (CTR) mode. This class allows for the initialization of a cryptographic engine with various parameters and provides properties to access important information about the encryption setup.

## Initialization

The class constructor (`__init__`) takes several parameters:

- `algorithm`: The encryption algorithm, currently supporting only 'AES'.
- `algorithm_depth`: The bit-depth of the encryption algorithm, supporting 128 or 256 bits.
- `mode`: The encryption mode, supporting 'CBC' (Cipher Block Chaining) or 'CTR' (Counter).
- `nonce_depth`: The bit-depth of the nonce, supporting 128 or 256 bits.
- `fixed_nonce`: A boolean indicating whether a fixed nonce should be used.
- `key`: The encryption key, provided as a string, bytes, or `None`. If not provided, a random key is generated.
- `nonce`: The nonce value, provided as a string, bytes, or `None`. If not provided, a random nonce is generated.

The constructor validates the provided parameters, raises exceptions for invalid inputs, and initializes the cryptographic engine based on the chosen algorithm and mode.

## Properties

The class provides several read-only properties to access information about the encryption setup:

- `algorithm`: Returns the encryption algorithm ('AES').
- `algorithm_depth`: Returns the bit-depth of the encryption algorithm.
- `engine`: Returns the cryptographic engine based on the selected algorithm and mode.
- `fixed_nonce`: Returns a boolean indicating whether a fixed nonce is used.
- `key`: Returns the encryption key.
- `mode`: Returns the encryption mode ('CBC' or 'CTR').
- `nonce`: Returns the nonce value.
- `nonce_depth`: Returns the bit-depth of the nonce.

## Exception Handling

The constructor raises exceptions for the following cases:

- Unsupported algorithm or mode.
- Invalid algorithm depth or nonce depth.
- Invalid data type for key or nonce.
- Dubious nonce settings (when using fixed nonce or not, but with inappropriate values).

## Random Generation

If a key or nonce is not provided during initialization, random values are generated using the `urandom` function from the `os` module.

Please note that this class utilizes the `cryptography` library for cryptographic operations and follows best practices for secure key and nonce generation.


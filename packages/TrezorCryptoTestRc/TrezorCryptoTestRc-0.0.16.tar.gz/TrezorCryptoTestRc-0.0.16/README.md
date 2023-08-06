# trezor-crypto

[![Build Status](https://travis-ci.org/trezor/trezor-crypto.svg?branch=master)](https://travis-ci.org/trezor/trezor-crypto) [![gitter](https://badges.gitter.im/trezor/community.svg)](https://gitter.im/trezor/community)

Heavily optimized cryptography algorithms for embedded devices.

These include:
- AES/Rijndael encryption/decryption
- Big Number (256 bit) Arithmetics
- BIP32 Hierarchical Deterministic Wallets
- BIP39 Mnemonic code
- ECDSA signing/verifying (supports secp256k1 and nist256p1 curves,
  uses RFC6979 for deterministic signatures)
- ECDSA public key derivation
- Base32 (RFC4648 and custom alphabets)
- Base58 address representation
- Ed25519 signing/verifying (also SHA3 and Keccak variants)
- ECDH using secp256k1, nist256p1 and Curve25519
- HMAC-SHA256 and HMAC-SHA512
- PBKDF2
- RIPEMD-160
- SHA1
- SHA2-256/SHA2-512
- SHA3/Keccak
- BLAKE2s/BLAKE2b
- Chacha20-Poly1305
- unit tests (using Check - check.sf.net; in test_check.c)
- tests against OpenSSL (in test_openssl.c)
- integrated Wycheproof tests

Distibuted under MIT License.

## Python support

The python bindings are updated and work with cython. Run the following commands to install the module. 
A prerequisite is pipenv is required

```bash
sudo apt install pipenv
```

Clone the repo and follow the instructions to install the package into your virtual environment:
If you have python 3.10 by default (Ubuntu 22.04 ships with it), you need to install ``python3.9`` and do the following:
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
sudo apt install libpython3.9-dev
sudo apt-get install python3.9-distutils
git clone git@github.com:RiddleAndCode/wallet2.git
git checkout trezorcrypto-cython-dev
cd wallet2/crypto
python3.9 -m pipenv sync
python3.9 -m pipenv shell

## Proceed to build the package as .whl under /dist
pip  install --upgrade pip wheel setuptools
python setup.py bdist_wheel
pip install  dist/TrezorCrypto-0.0.1-cp39-cp39-linux_x86_64.whl 

## run the tests
python tests/bip32_tests.py 
```

If you already have `python3.9` just do the following:
```bash
git clone git@github.com:RiddleAndCode/wallet2.git
git checkout trezorcrypto-cython-dev
cd wallet2/crypto
python3.9 -m pipenv sync
python3.9 -m pipenv shell

pip  install --upgrade pip wheel setuptools

## Proceed to build the package as .whl under /dist and install with pip later on

python setup.py bdist_wheel
pip install  dist/TrezorCrypto-0.0.1-cp39-cp39-linux_x86_64.whl 

## run the tests
python tests/bip32_tests.py

```
The current support is limited. A basic test can be performed as follows
```bash
python tests/keydrivation.py
```



## Some parts of the library come from external sources:

- AES: https://github.com/BrianGladman/aes
- Base58: https://github.com/luke-jr/libbase58
- BLAKE2s/BLAKE2b: https://github.com/BLAKE2/BLAKE2
- RIPEMD-160: https://github.com/ARMmbed/mbedtls
- SHA1/SHA2: http://www.aarongifford.com/computers/sha.html
- SHA3: https://github.com/rhash/RHash
- Curve25519: https://github.com/agl/curve25519-donna
- Ed25519: https://github.com/floodyberry/ed25519-donna
- Chacha20: https://github.com/wg/c20p1305
- Poly1305: https://github.com/floodyberry/poly1305-donna

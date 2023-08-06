#!python
#cython: language_level=3

cimport c
cimport cython
from libc.stdint cimport uint32_t
from libc.string cimport memset

from typing import *

SECP256K1_NAME = c.SECP256K1_NAME
SECP256K1_DECRED_NAME = c.SECP256K1_DECRED_NAME
SECP256K1_GROESTL_NAME = c.SECP256K1_GROESTL_NAME
SECP256K1_SMART_NAME = c.SECP256K1_SMART_NAME
NIST256P1_NAME = c.NIST256P1_NAME
ED25519_NAME = c.ED25519_NAME
ED25519_CARDANO_NAME = c.ED25519_CARDANO_NAME
ED25519_SHA3_NAME = c.ED25519_SHA3_NAME
ED25519_KECCAK_NAME = c.ED25519_KECCAK_NAME
CURVE25519_NAME = c.CURVE25519_NAME


cdef class HDNode:
    """
    BIP0032 HD node structure.
    """
    cdef c.HDNode node  # is this reference as self ?
    cdef uint32_t _fingerprint
    def __init__(
            self,
            depth: int,
            fingerprint: int,
            child_num: int,
            chain_code: bytes,
            private_key: bytes | None = None,
            public_key: bytes | None = None,
            curve_name: str | None = None,
    ):
        if len(chain_code) != 32:
            raise ValueError("chain code id length should be 32 bytes, yours is  ", len(chain_code))
        if 0 == len(public_key) and 0 == len(private_key):
            raise ValueError("Either public_key or private_key is required")
        if 0 != len(private_key) and 32 != len(private_key):
            raise ValueError("Private_key is invalid")
        if 0 != len(public_key) and 33 != len(public_key):
            raise ValueError("Private_key is invalid")

        cdef const c.curve_info * curve = NULL
        if 0 == len(curve_name):
            curve = c.get_curve_by_name(c.SECP256K1_NAME)  # TODO check if ptr is correct
        else:
            curve = c.get_curve_by_name(curve_name.encode()) # TODO

        if curve is NULL:
            raise ValueError("Curve_name is invalid")

        self._fingerprint = fingerprint
        self.node.depth = depth
        self.node.child_num = child_num
        self.node.curve = curve

        if 32 == len(chain_code):
            self.node.chain_code = chain_code
        else:
            self.node.chain_code = bytes(32)
        if 32 == len(private_key):
            self.node.private_key = private_key
        else:
            self.node.private_key = bytes(32)

        if 33 == len(public_key):
            self.node.public_key = public_key
        else:
            self.node.public_key = bytes(33)

    def __init__(self, seed: bytes, curve_name):
        cdef int i = c.hdnode_from_seed(seed,len(seed), curve_name, cython.address(self.node))
        self._fingerprint = 0
        if i == 0:
            raise ValueError("HDNode from seed failed! ")


    def derive(self, index: int, public: bool = False) -> None:
        """
        Derive a BIP0032 child node in place.
        """
        cdef uint32_t fp = c.hdnode_fingerprint(cython.address(self.node))
        self._fingerprint = fp
        cdef int res = 0;
        if public:
            res = c.hdnode_public_ckd(cython.address(self.node),index)
        else:
            if self.node.private_key == bytes(32):
                memset(cython.address(self.node),0, cython.sizeof(self.node))
                raise ValueError("Failed to derive, private key not set")
            res = c.hdnode_private_ckd(cython.address(self.node),index)
        if res == 0:
            memset(cython.address(self.node),0, cython.sizeof(self.node))
            raise ValueError("Failed to derive, private key not set")



    def derive_path(self, path: Sequence[int]) -> None:
        """
        Go through a list of indexes and iteratively derive a child node in
        place.
        """

        plen = len(path) # TODO check what Sequence is
        if plen > 32:
            raise ValueError("Path can not be longer than 32 indexes")
        for pi in range(plen):
            if pi == (plen - 1):
                # fingerprint is calculated from the parent of the final derivation
                self._fingerprint = c.hdnode_fingerprint(cython.address(self.node))
            pitem = path[pi]
            if c.hdnode_private_ckd(cython.address(self.node), pitem) == 0:
                self._fingerprint = 0
                memset(cython.address(self.node),0, cython.sizeof(self.node))
                raise ValueError("Failed to derive path")


    def serialize_public(self, version: int) -> str:
        """
        Serialize the public info from HD node to base58 string.
        """
        cdef char[120] buffer
        cdef int written = c.hdnode_serialize_public(cython.address(self.node), self._fingerprint, version, buffer, 120)
        pubkey_string = buffer.decode("utf-8")
        return pubkey_string


    def serialize_private(self, version: int) -> str:
        """
        Serialize the public info from HD node to base58 string.
        """
        cdef char[120] buffer
        cdef int written = c.hdnode_serialize_private(cython.address(self.node), self._fingerprint, version, buffer, 120)
        private_key_string = buffer.decode("utf-8")
        return private_key_string


    def clone(self) -> HDNode:
        """
        Returns a copy of the HD node.
        """
        return HDNode(self.depth(), self._fingerprint,self.child_num(),self.chain_code(),self.public_key(),self.public_key(),str(self.node.curve.bip32_name))

    def depth(self) -> int:
        """
        Returns a depth of the HD node.
        """
        return self.node.depth

    def fingerprint(self) -> int:
        """
        Returns a fingerprint of the HD node (hash of the parent public key).
        """
        return self._fingerprint

    def child_num(self) -> int:
        """
        Returns a child index of the HD node.
        """
        return self.node.child_num

    def chain_code(self) -> bytes:
        """
        Returns a chain code of the HD node.
        """
        cdef uint32_t array_len = cython.sizeof(self.node.chain_code)
        return self.node.chain_code[:array_len]


    def private_key(self) -> bytes:
        """
        Returns a private key of the HD node.
        """
        cdef uint32_t array_len = cython.sizeof(self.node.private_key)
        return self.node.private_key[:array_len]

    def private_key_ext(self) -> bytes:
        """
        Returns a private key extension of the HD node.
        """
        cdef uint32_t  array_len = cython.sizeof(self.node.private_key_extension)
        return self.node.private_key_extension[:array_len]


    def public_key(self) -> bytes:
        """
        Returns a public key of the HD node.
        """
        c.hdnode_fill_public_key(cython.address(self.node))
        cdef uint32_t  array_len = cython.sizeof(self.node.public_key)
        return self.node.public_key[:array_len]

        ## TODO you can not return it directly like this, you need the bytearray from of this



    def address(self, version: int) -> str:
        """
        Compute a base58-encoded address string from the HD node.
        """
        cdef char[40] buffer
        c.hdnode_get_address(cython.address(self.node), version, buffer, 40)
        return str(buffer)

    def nem_address(self, network: int) -> str:
        """
        Compute a NEM address string from the HD node.
        """

    def nem_encrypt(
            self, transfer_public_key: bytes, iv: bytes, salt: bytes, payload: bytes
    ) -> bytes:
        """
        Encrypts payload using the transfer's public key
        """

    def ethereum_pubkeyhash(self) -> bytes:
        """
        Compute an Ethereum pubkeyhash (aka address) from the HD node.
        """

    def __del__(self) -> None:
        """
        Cleans up sensitive memory.
        """

# extmod/modtrezorcrypto/modtrezorcrypto-bip32.h

def from_seed(seed: bytes, curve_name) -> HDNode:
    if len(seed) == 0:
        raise ValueError("Invalid seed")
    if len(curve_name) == 0:
        raise ValueError("Invalid curve name")
    return HDNode(seed, curve_name)




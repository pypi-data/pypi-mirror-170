from libc.stdint cimport uint32_t, uint8_t

cdef extern from "curves.h":
    extern const char SECP256K1_NAME[]
    extern const char SECP256K1_DECRED_NAME[]
    extern const char SECP256K1_GROESTL_NAME[]
    extern const char SECP256K1_SMART_NAME[]
    extern const char NIST256P1_NAME[]
    extern const char ED25519_NAME[]
    extern const char ED25519_CARDANO_NAME[]
    extern const char ED25519_SHA3_NAME[]
    extern const char ED25519_KECCAK_NAME[]
    extern const char CURVE25519_NAME[]


cdef extern from "bignum.h":
    ctypedef struct bignum256:
        uint32_t val[9];



cdef extern from "ecdsa.h":
    ctypedef struct  curve_point:
        bignum256 x, y

    ctypedef struct ecdsa_curve:
        bignum256 prime;  # prime order of the finite field
        curve_point G  # initial curve point
        bignum256 order  # order of G
        bignum256 order_half;  # order of G divided by 2
        int a  # coefficient 'a' of the elliptic curve
        bignum256 b  # coefficient 'b' of the elliptic curve
        const curve_point cp[64][8];

#if USE_PRECOMPUTED_CP
#  const curve_point cp[64][8];
#endif


cdef extern from "bip32.h":
    #	ctypedef struct HDNode:
    #		uint8_t public_key[33]
    #
    #	typedef struct {
    #	const char *bip32_name;     // string for generating BIP32 xprv from seed
    #	const ecdsa_curve *params;  // ecdsa curve parameters, null for ed25519
    #
    #	HasherType hasher_base58;
    #	HasherType hasher_sign;
    #	HasherType hasher_pubkey;
    #	HasherType hasher_script;
    #	} curve_info;

    ctypedef struct HDNode:
        uint32_t depth
        uint32_t child_num
        uint8_t public_key[33]
        uint8_t chain_code[32]
        uint8_t private_key[32]

        uint8_t private_key_extension[32]

        const curve_info *curve;

    ctypedef struct curve_info:
        const char *bip32_name;  # string for generating BIP32 xprv from seed
        const ecdsa_curve *params  # ecdsa curve parameters, null for ed25519
        HasherType hasher_base58
        HasherType hasher_sign
        HasherType hasher_pubkey
        HasherType hasher_script

    int hdnode_from_seed(const uint8_t *seed, int seed_len, const char *curve,
                         HDNode *out);

    int hdnode_private_ckd(HDNode *inout, uint32_t i);

    int hdnode_public_ckd(HDNode *inout, uint32_t i);

    int hdnode_serialize_public(const HDNode *node, uint32_t fingerprint,
                                uint32_t version, char *str, int strsize);

    int hdnode_serialize_private(const HDNode *node, uint32_t fingerprint,
                                 uint32_t version, char *str, int strsize);

    int hdnode_deserialize_public(const char *str, uint32_t version,
                                  const char *curve, HDNode *node,
                                  uint32_t *fingerprint);

    int hdnode_deserialize_private(const char *str, uint32_t version,
                                   const char *curve, HDNode *node,
                                   uint32_t *fingerprint);

    void hdnode_fill_public_key(HDNode *node);

    void hdnode_get_address(HDNode *node, uint32_t version, char *addr,
                            int addrsize);

    const curve_info * get_curve_by_name(const char * curve_name);

    uint32_t hdnode_fingerprint(HDNode *node);

cdef extern from "base58.h":
    #define HASHER_DIGEST_LENGTH 32

    cpdef enum HasherType:
        HASHER_SHA2 = 0
        HASHER_SHA2D,
        HASHER_SHA2_RIPEMD,

        HASHER_SHA3,
        HASHER_SHA3K,

        HASHER_BLAKE,
        HASHER_BLAKED,
        HASHER_BLAKE_RIPEMD,

        HASHER_GROESTLD_TRUNC,

        HASHER_BLAKE2B,
        HASHER_BLAKE2B_PERSONAL

    int base58_encode_check(const uint8_t *data, int len, HasherType hasher_type,
                            char *str, int strsize);

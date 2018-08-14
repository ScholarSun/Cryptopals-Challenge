import binascii

def fixed_xor(s1,s2):
    byte_seq1 = binascii.unhexlify(s1)
    byte_seq2 = binascii.unhexlify(s2)

    print(byte_seq2)
    print(byte_seq1)

    return binascii.hexlify(bytes(a ^ b for a, b in zip(byte_seq1, byte_seq2)))
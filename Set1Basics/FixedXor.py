import binascii


def fixed_xor(s1, s2):
    byte_seq1 = binascii.unhexlify(s1)
    byte_seq2 = binascii.unhexlify(s2)
    return binascii.hexlify(bytes(a ^ b for a, b in zip(byte_seq1, byte_seq2)))


def main():
    input1 = "1c0111001f010100061a024b53535009181c"
    input2 = "686974207468652062756c6c277320657965"
    print(fixed_xor(input1, input2))
    assert (fixed_xor(input1, input2) == b'746865206b696420646f6e277420706c6179')

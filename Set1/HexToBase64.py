import base64
import binascii


# Converts hex to base 64
def hex_to_base64(s):
    byte_seq = binascii.unhexlify(s)
    return base64.b64encode(byte_seq)


def main():
    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    assert (hex_to_base64(input) == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

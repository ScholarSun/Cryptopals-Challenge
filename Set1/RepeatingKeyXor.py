import binascii


# Function that XORs a single character given a key
def apply_xor(char, key_inc, key):
    if key_inc[0] == len(key):
        key_inc[0] = 0
    xored = ord(char) ^ ord(key[key_inc[0]])
    key_inc[0] += 1

    return xored


# Applies repeating xor on a string
def repeating_key_xor(s, key):
    # Incrementor to track index of key
    key_inc = [0]

    # Generate ciphertext
    ciphertext = binascii.hexlify(bytearray([apply_xor(x, key_inc, key) for x in s]))
    return ciphertext


def main():
    ciphertext = repeating_key_xor("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE")
    print(ciphertext)
    assert (
    ciphertext == b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')

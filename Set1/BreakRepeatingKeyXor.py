import base64
from Set1.BreakSingleByteXor import *
from Set1.RepeatingKeyXor import *

# Possible combinations for key size calculation
key_combo = [[0, 1, 1, 2], [0, 1, 2, 3], [0, 1, 3, 4], [1, 2, 2, 3], [1, 2, 3, 4], [2, 3, 3, 4]]


# Computes the hamming distance (bits)
def hamming_distance(seq1, seq2, isbyte):
    distance = 0

    # Binary convert for string and bytes
    if isbyte:
        seq1 = ''.join(format(x, '08b') for x in seq1)
        seq2 = ''.join(format(x, '08b') for x in seq2)
    else:
        seq1 = ''.join(format(ord(x), '08b') for x in seq1)
        seq2 = ''.join(format(ord(x), '08b') for x in seq2)

    # Counting differences
    for a, b in zip(seq1, seq2):
        if a != b:
            distance += 1
    return distance


# Break repeating XOR
def break_repeating_xor(ciphertext):
    listofscores = []
    ciphertext = base64.b64decode(ciphertext)
    possible_keys = []

    # Find keysize, 4 byte division
    for keysize in range(1, 41):
        if keysize * 4 > len(ciphertext):
            break
        score = 0

        # Compute hamming distance for all possible combination of bytes
        for x in key_combo:
            score += hamming_distance(ciphertext[keysize * x[0]:keysize * x[1]],
                                      ciphertext[keysize * x[2]:keysize * x[3]], True)

        # Normalize
        listofscores.append(((score / 6) / keysize, keysize))

    # Top 4 possible keysizes
    possible_key_sizes = [x[1] for x in sorted(listofscores)[:4]] \
 \
        # Checks possible key sizes
    for ks in possible_key_sizes:
        plaintextkey = []

        # Divides the ciphertext into blocks of ks sizes and finds key value
        for index in range(ks):
            # Partition
            partitioned = [ciphertext[i] for i in range(index, len(ciphertext), ks)]

            # Conversion
            byt = bytes(partitioned)
            hex = binascii.hexlify(byt)

            # Builds upon the key
            plaintextkey.append(chr(single_byte_xor_cipher(hex)[1]))
        key = ''.join(plaintextkey)
        possible_keys.append(key)

    high_score = 0
    best_key = ''
    plaintext = ''

    # Uses the possible keys to decrypt message and scores them
    for key in possible_keys:
        message = binascii.unhexlify(repeating_key_xor(ciphertext.decode('ascii'), key))
        score = score_val('', '', message.decode(), True)
        if score > high_score:
            high_score = score
            plaintext = message
            best_key = key
    plaintext = plaintext.decode("ascii")
    return plaintext, best_key


def main():
    with open('Data/repeatingxor.txt', 'r') as myfile:
        data = myfile.read()
    plaintext = break_repeating_xor(data)[0]
    print(plaintext)

    assert (hamming_distance("this is a test", "wokka wokka!!!", False) == 37)
    assert (plaintext[:33] == "I'm back and I'm ringin' the bell")

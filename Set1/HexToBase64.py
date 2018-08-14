import base64
from .BreakSingleByteXor import *

def hex_to_base64(s):
    byte_seq = binascii.unhexlify(s)
    return base64.b64encode(byte_seq)

def apply_xor(char,key_inc,key):
    if key_inc[0] == len(key):
        key_inc[0] = 0
    #print(char)
    #print(key[key_inc[0]])
    xored = ord(char)^ord(key[key_inc[0]])
    key_inc[0]+=1
    return xored

def repeating_key_xor(s,key):
    key_inc = [0]
    encrypted = binascii.hexlify(bytearray([apply_xor(x,key_inc,key) for x in s]))
    return encrypted

def hamming_distance(seq1,seq2):
    distance = 0
    #print(seq1)
    #print(base64.b64decode(seq1))
    seq1 = ''.join(format(x, '08b') for x in seq1)
    seq2 = ''.join(format(x, '08b') for x in seq2)
    print(seq1)
    print(seq2)
    for a,b in zip(seq1,seq2):
        if a != b:
            distance+=1
    print(distance)
    return distance

def break_repeating_xor(ciphertext):
    listofscores = []
    ciphertext = base64.b64decode(ciphertext)
    #print(ciphertext)
    for keysize in range(1,41):
        if keysize*4 > len(ciphertext):
            break
        score = 0
        for x in range (1,4):
            score += hamming_distance(ciphertext[keysize*(x-1):keysize*x],ciphertext[keysize*x:keysize*(x+1)])
        score += hamming_distance(ciphertext[:keysize],ciphertext[keysize*2:keysize*3])
        score += hamming_distance(ciphertext[:keysize], ciphertext[keysize * 3:keysize * 4])
        score += hamming_distance(ciphertext[keysize:keysize*2], ciphertext[keysize * 3:keysize * 4])
        #print(score)
        listofscores.append(((score/6)/keysize,keysize))
    print(sorted(listofscores))
    possible_key_sizes = [x[1] for x in sorted(listofscores)[:4]]

    print(listofscores)
    print(possible_key_sizes)

    possible_keys = []
    for ks in possible_key_sizes:
        plaintextkey = []
        for index in range(ks):
            partitioned = [ciphertext[i] for i in range(index, len(ciphertext), ks)]
            #print(partitioned)
            byt = bytes(partitioned)
            #print(byt)
            hex = binascii.hexlify(byt)
            #print(hex)
            plaintextkey.append(chr(single_byte_xor_cipher(hex)[1]))
        stringy = ''.join(plaintextkey)
        possible_keys.append(stringy)
        #print(plaintextkey)

    for key in possible_keys:
        message = binascii.unhexlify(repeating_key_xor(ciphertext.decode('ascii'),key))
        score = score_val('', '', message.decode(), True)
        print(key)
        print(score)
        print(message.decode('ascii'))



    #return



# Hex to base64 tests
#input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#print(hex_to_base64(input))




# Detect_xor
#detect_xor()

# Repeating key XOR
#print(base64.b64encode(binascii.unhexlify(repeating_key_xor("This module provides data encoding and decoding as specified in RFC 3548. This standard defines the Base16, Base32, and Base64 algorithms for encoding and decoding arbitrary binary strings into ASCII-only byte strings that can be safely sent by email, used as parts of URLs, or included as part of an HTTP POST request. The encoding algorithm is not the same as the uuencode program.","WASSUPSHORTY"))))

#print(hamming_distance("this is a test","wokka wokka!!!"))
#break_repeating_xor("testdf sdfawef fewa")
#with open('Data/repeatingxor.txt', 'r') as myfile:
#  data = myfile.read()
#print(break_repeating_xor(data))

break_repeating_xor("Ayk6IHU9PCw6PjF5JzM8JTw0NjtvNjUtNmE2PTY/NyEhNXQ4OSVzNzAzPCwmPDN5NjJzICU1MCEpOzE9dyg9cwcWEGh8Z2BheWEHOzwjczs7Mzo9NjM3czE1NSEhNyd5Iyk2cxcxIC1+ZHh5FSAgNmZif2guPDB5FSAgNmNkcykjNTsrPjU7PiZwNSc9cjE3NC43Ojs3cykhNnQ9MiI8Nzw+NGguIDYwIzMyISxwMSEhMyYgdzInITw+NDtvOzotOGESABYZGmUgPDggdyMqJzBwIDw9Ozo+JGEnOzQkcysuPHQ7MmEgMjM1PzFvITE3I2ExKnU1PikmPnh5IjI2N3UxIGg/MyYtJGE8NXUFAQQ8fnQ2JWE6PTY8JiwqNnQ4JGEjMickcycpcjU3dwkHBwVwAwccBnQrMjAmNiYkfWgbOjF5Mi8wPDE5PS9vMzg+ODM6Jz09cyE8cjo2I2EnOzBwICkiN3Q4JGEnOzBwJj0qPDc2MyRzIyc/NDouP3o==")
#break_repeating_xor("ABCDEFGHIJKLMNO")
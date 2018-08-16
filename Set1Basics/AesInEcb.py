from Crypto.Cipher import AES
import base64


# AES decrypt method
def aes_decrypt(ciphertext, key):
    # Convert to bytes
    key = key.encode()
    ciphertext = base64.b64decode(ciphertext)

    # AES object decrpyt through library
    cipher_object = AES.new(key, AES.MODE_ECB)
    plaintext = cipher_object.decrypt(ciphertext).decode('ascii')
    return plaintext


def main():
    with open('Data/aestext.txt', 'r') as myfile:
        data = myfile.read()
    plaintext = aes_decrypt(data, "YELLOW SUBMARINE")

    print(plaintext)
    assert (plaintext[:33] == "I'm back and I'm ringin' the bell")

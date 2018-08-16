# Performs PKCS7 padding
def pkcs7_padding(message,block_len):
    # Calculates how much to pad
    remainder = len(message)%block_len
    to_pad = 0

    # Checks 0 remainder
    if remainder == 0:
        to_pad = 0
    else:
        to_pad = block_len - remainder

    # Convert to bytearray
    barray = bytearray()
    barray.extend(message.encode())

    # Append padding
    append_val = to_pad
    for x in range(to_pad):
        barray.append(append_val)
    return barray

def main():
    assert(pkcs7_padding("YELLOW SUBMARINE",20) == b'YELLOW SUBMARINE\x04\x04\x04\x04')
    print(pkcs7_padding("YELLOW SUBMARINE",20))

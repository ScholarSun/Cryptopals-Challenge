from Set1.BreakSingleByteXor import score_val,single_byte_xor_cipher

# Given the file, detects the line that has been XOR ciphered
def detect_xor():
    file = open("Data/cryptoxorinputs.txt", "r")
    highscore = 0
    bestline = ""

    # Reads each line and scores
    for line in file:
        # Stops at end of file
        if len(line)%2 == 0:
            break

        # Truncates to remove \n characters
        plaintext = single_byte_xor_cipher(line[:-3])[0]

        # Scores
        score = score_val('','',plaintext,True)
        if score > highscore:
            highscore = score
            bestline = plaintext
    return bestline

def main():
    print(detect_xor())
    assert(detect_xor() == "Now that the party is jumping")

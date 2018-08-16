from collections import Counter

# Detect AES-ECB encryption
def detect_aes():
    # Reads each line and scores
    file = open("Data/hexaes.txt", "r")
    for line in file:
        has_dupe = False

        # Stops at end of file
        if len(line) % 2 == 0:
            break

        # Removes new line
        line = line[:-1]

        # Partitions into 16
        partitioned = [line[i:i+16] for i  in range(0, len(line), 16)]

        # Frequnecy Counter
        frequnecy = Counter (partitioned)
        for x in frequnecy:
            if frequnecy.get(x) != 1:
                has_dupe = True

        # Print suspected line
        if has_dupe:
            print(frequnecy)


def main():
    detect_aes()
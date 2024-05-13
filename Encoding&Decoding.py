import random
def CyberCryptor():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']',
               'K': '1',
               'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5',
               'V': '!',
               'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D',
               '7': 'E',
               '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ': '_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J',
               '1': 'K',
               '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U',
               '!': 'V',
               '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6',
               'E': '7',
               '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}
    answer = "Y"
    while answer == "Y":
        input_code= input("Insert a message: ")
        new_input= input_code.upper()
        process= input("Encode(E) or Decode(D)? ")
        if process.upper() == "E" :
            print("Encoded message:")
            for x in new_input :
                if x in encoder.keys():
                    print(encoder[x],end="")
        elif process.upper() == "D" :
            print("Decoded message:")
            for x in new_input :
                if x in decoder.keys():
                    print(decoder[x],end="")
        answer = input("\nEncode/decode again [Y/N]? ").upper()


def random_set():
    numCount = 0
    numSet = set()
    while len(numSet) < 5:
        num = random.randint(1, 20)
        if num not in numSet:
            numSet.add(num)
    return numSet



def print_set(aSet, prompt=""):
    print(prompt, end="")
    for s in aSet:
        print(s, end=" ")
    print('\n')


def main():

    print("\n---- Encoder/Decoder ----")
    CyberCryptor()


if __name__ == "__main__":
    main()

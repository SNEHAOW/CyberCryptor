################################
# EECS1015, York University
# Lab 5 starting code
# Name:  Sadia Tasnim Sneha
# Section:  B
# Student ID: 219536093
# Email:  sneha002@my.yorku.ca
################################

import random


# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Sadia Tasnim Sneha")
    print("Section B")
    print("Student id: 219536093")
    print("Email: sneha002@my.yorku.ca")


def task0():
    # Example of calling a function from taskX() functions.
    # you should write all functions "outside" your task1()-task4() functions.
    print_lab_info()


def task1():
    def input_list():
        list = []
        user_input = int(input("Input positive int: "))
        while user_input >= 0:
            list.append(user_input)
            user_input = int(input("Input positive int: "))
        return list

    def compute_average(aList):
        sum= 0
        for i in aList :
            sum= sum + i
        average= float(sum/2)
        if (list==[]):
            return 0
        else:
            return average
    repeat = "Y"
    while repeat == "Y" :
        the_list= input_list()
        average=compute_average(the_list)
        print(f"List average {average:.2f}")
        repeat=input("Do again [Y/N]? ").upper()




def task2():
    string = input("Input a long string: ").upper()
    s_list = list(string)
    s_set = set(string)
    s_Dictionary = {}
    for element in s_set:
        s_Dictionary[element]=0

    for i in s_list:
        s_Dictionary[i]+=1

    for j in s_Dictionary:
        print(f"\'{j}\' | {'*'*s_Dictionary[j]}")


def task3():
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


def task4():
    choice = 'y'

    while choice.lower() == 'y':
        userNumSet = set()
        while len(userNumSet) != 5:
            numStr = input('Enter 5 numbers between 1-20: ')
            numList = numStr.split(' ')
            userNumSet = set()
            for n in numList:
                userNumSet.add(int(n))
        computerNumSet = random_set()
        print_set(computerNumSet, 'Computers numbers: ')
        matchCount = 0
        matches = []
        for n1 in userNumSet:
            if n1 in computerNumSet:
                matchCount += 1
                matches.append(n1)
        if matchCount > 0:
            print_set(matches, str(matchCount) + ' matches found: ')
            if matchCount == 5:
                print('YOU WIN!')
        else:
            print('NO MATCHES!!')
        choice = input('Try again [Y/N]? ')


def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()


if __name__ == "__main__":
    main()
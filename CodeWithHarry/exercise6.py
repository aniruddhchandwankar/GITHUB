#! "C:\Users\Aniruddh\AppData\Local\Programs\Python\Python38\python.exe"

import random

attempts = 10
print("Choose from one of the following\nR = Rock\nP = Paper\nS = Scissor\n")

def computers_choice():
    a = ["R", "P", "S"]
    random1 = random.choice(a)
    return random1

def your_choice():
    a = str(input("Enter your choice: "))
    return a

i = 0
j = 0
k = 0
attempts1 = 11


while True:
    if attempts1 >0:
        attempts1 = attempts1 - 1
        print(f"Attempts left: {attempts1}\n")
        his = computers_choice()
        yours = your_choice()
        yours = yours.lower()
        yours = yours.capitalize()
        print(f"\nComputer selected: {his}")
        if yours == his:
            print("\n---------------------------\n")
            print("######### Please try again! ##########")
            print("\n---------------------------\n")
            attempts1 = attempts1 + 1
        elif (yours == "R" and his == "S") or \
             ((yours == "P" and his == "R")) or \
             (yours == "S" and his == "P"):
            i = i + 1
            print("\n***************************")
            print(f"You won {i} times")
            print(f"You lost {j} times")
            print("***************************\n")

        else:
            j = j + 1
            print("\n***************************")
            print(f"You won {i} times")
            print(f"You lost {j} times")
            print("***************************\n")
    else:
        if i >5:
            print("You WON, Game Over!")
        else:
            print("You LOST, Game Over!")
        break









import random
attempts = 10

def computers_choice():
    a = ["R", "P", "S"]
    random1 = random.choice(a)
    return random1

def your_choice():
    print("Choose from one of the following\nR = Rock\nP = Paper\nS = Scissor\n")
    a = str(input("Enter your choice: "))
    return a

i = 0
j = 0
attempts1 = 10


while True:
    if attempts1 >0:
        his = computers_choice()
        yours = your_choice()
        yours = yours.lower()
        yours = yours.capitalize()
        print(f"Computer selected {his}")
        if yours == his:
            i = i + 1
            print("\n***************************\n")
            print(f"You won {i} times")
            print(f"You lost {j} times")
            print("\n***************************\n")
        else:
            j = j + 1
            print("\n***************************\n")
            print(f"You won {i} times")
            print(f"You lost {j} times")
            print("\n***************************\n")
        attempts1 = attempts1 - 1
        print(f"Attempts left: {attempts1}")
        print ("\n***************************\n")
    else:
        if i >5:
            print("You WON, Game Over!")
        else:
            print("You LOST, Game Over!")
        break







#     you = input("Enter your choice: ")
#     yourcount  = you.count()
#     if you == random1:
#         times_won = yourcount + 1
#
# yourchoice()








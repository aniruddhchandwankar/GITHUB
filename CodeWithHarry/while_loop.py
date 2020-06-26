
# No of guesses 9
# print no guess left
# No of guesses he took to finish
# Game over if not done within given attempts


n = 20
attempts = 5



#   Match n to i
# Successful attempt
#attempts > 0

while(1):
    if attempts > 0:
        print("Number of attempts left", attempts)
        i = int(input("Enter your number: "))
        if i == n:  #(If true  condition)
            print("You have won")
            print("Game over")
            break
        else:
            if i < n and attempts > 1: #(If false condition)
               #(Smaller condition)
                print("Your number is smaller than magic number ")
                print("Please try again!")
                #attempts = attempts - 1

            if i > n and attempts > 1: # (Greater condition)
                print("Your number is greater than magic number ")
                print("Please try again!")
                #attempts = attempts - 1
            attempts = attempts - 1
    else:
        print("Game Over, you have lost!")
        break
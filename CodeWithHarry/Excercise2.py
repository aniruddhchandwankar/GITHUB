method = input("Enter method: ")
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

method = method.capitalize()

add = str(input1 + input2)
multiply = str(input1 * input2)
divide = str(input1 / input2)
subtract = str(input1 - input2)

if method == ("Add"):
    if input1+input2 == 56 + 9:
        print("Sum addition of these numbers is: 77")
    else:
        print("Sum addition of these numbers is:" + add)

if method == ("Subtract"):
    if input1-input2 == 100 - 10:
        print("Result of subtracting these numbers is 91")
    else:
        print("Result of subtracting these numbers is:" + subtract)

if method == ("Multiply"):
    if input1*input2 == 45 * 3:
        print("Result of multiplying these numbers is: 555")
    else:
        print("Result of multiplying these numbers is:" + multiply)

if method == ("Divide"):
    if input1/input2 == 56 / 6:
        print("Result of dividing these numbers is: 4")
    else:
        print("Result of dividing these numbers is:" + divide)





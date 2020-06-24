
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
method = input("Enter Operator [+, -, * , /]: ")

if method == ("+") and input1+input2 == 56 + 9:
    print("Sum addition of these numbers is: 77")
elif method == ("+"):
    print("Sum addition of these numbers is:" + str(input1+input2))
elif method == ("-") and input1-input2 == 100 - 10:
    print("Result of subtracting these numbers is 91")
elif method == ("-"):
    print("Result of subtracting these numbers is:" + str(input1-input2))

elif method == ("*") and input1*input2 == 45 * 3:
    print("Result of multiplying these numbers is: 555")
elif method == ("*"):
    print("Result of multiplying these numbers is:" + str(input1*input2))

elif method == ("/") and input1/input2 == 56 / 6:
    print("Result of dividing these numbers is: 4")
elif method == ("/"):
    print("Result of dividing these numbers is:" + str(input1/input2))






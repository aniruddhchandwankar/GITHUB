age = int(input("Enter your age: "))

ranges = *range (81, 100), *range(6, 18)

if age in range (19, 81):
    print ("You're eligible to drive")
elif age in ranges:
    print ("You're not eligible to drive")
else:
    print("Come here personally so we can decide whether you can drive or not")

#https://leancrew.com/all-this/2019/09/discontinuous-ranges-in-python/ "When you don't know how-tos just Google it :-)"
def getdate():
    import datetime
    return datetime.datetime.now()

def user():
    b = str(input("Please enter the name of user: "))
    b = b.lower()
    b = b.capitalize()
    return b

def type():
    c = str(input("Do you want to Log Exercise or Food: "))
    c = c.lower()
    c = c.capitalize()
    return c

# def break_seq():
#     y = str(input("Entry has been logged. Do you want to continue: "))
#     y = y.lower()
#     y = y.capitalize()

while (True):
    print("""Press '1' to Log user data\nPress '2' to Retrieve user data\nPress '3' to Exit""")
    a = int(input("Enter your Input: "))
    if a == 3:
        break
    if a == 1:
        username = str(user())
        log_type = str(type())
        if log_type == "Food":
            with open ("Food_"+username+".txt", "a") as f:
                date = str(getdate())
                f.write("[Date]") + f.write(date)
                f.write("\n")
                f.write(input("enter data: "))
                f.write("\n")
                input("Entry has been logged. Thank you!, press ENTER to continue")

        elif log_type == "Exercise":
            with open ("Exercise_"+username+".txt", "a") as f:
                date = str(getdate())
                f.write("[Date]") + f.write(date)
                f.write("\n")
                f.write(input("enter data: "))
                f.write("\n")
                input("Entry has been logged. Thank you!, press ENTER to continue")
    elif a == 2:
        username = str(user())
        log_type = str(type())
        if log_type == "Exercise":
            with open("exercise_"+username+".txt", "r") as f:
                f.seek(0)
                content = f.read()
                print(content)
                input("Hope you find the data useful, Thank you!. Press ENTER to continue")
        if log_type == "Food":
            with open("Food_"+username+".txt", "r") as f:
                f.seek(0)
                content = f.read()
                print(content)
                input("Hope you find the data useful, Thank you!. Press ENTER to continue")

print("Process completed. Thank you, Goodbye")

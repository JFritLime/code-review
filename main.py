name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))

if age >= 18:
    print(f"{name}, you are allowed to take a drivers licence!")
else:
    print(f"{name}, you are not allowed to take a drivers licence")
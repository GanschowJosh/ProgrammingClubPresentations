# Example program
import random

def checkNumber(n):
    print(f"Number is {n}")
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

while True:
    userInput = input("Would you like to generate a number? y/n: ")

    if userInput.lower() == "y":
        checkNumber(random.randint(1, 100))
    elif userInput.lower() == "n":
        print("Exiting program.")
        break
    else:
        print("Invalid input, please type y or n")



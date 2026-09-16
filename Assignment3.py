"""
Data Analytics (DA) - Module 4
Python Assignment 3: While Loop, For Loop, and Function
"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 3  

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    attempts -= 1
else:
    print("Better luck next time!")

# TASK 2: For Loop - Multiplication Table Generator

number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 101):
    print(f"{number} x {i} = {number * i}")


# TASK 3: Function - BMI Calculator

def calculate_bmi(weight, height):
    """Return BMI given weight in kg and height in meters."""
    return weight / (height ** 2)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

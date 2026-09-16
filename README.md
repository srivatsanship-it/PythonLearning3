# Python Assignment 3 – While Loop, For Loop, and Function

**Data Analytics Course | Module 4 – Python**

## Overview
This project demonstrates Python control flow and functions through three small programs: a number-guessing game (while loop + control statements), a multiplication table generator (for loop), and a BMI calculator (function).

## File
| File | Description |
|---|---|
| `Assignment3.py` | Complete, tested Python script covering all three tasks |

## Tasks Covered

### Task 1 – Number Guessing Game (While Loop)
- Generates a random secret number between 1 and 10 (`random.randint`)
- Allows 3 valid guesses via a `while` loop
- `continue` — skips an attempt (without using it up) if the guess is out of range
- `break` — exits the loop immediately on a correct guess
- `while...else` — prints "Better luck next time!" only if the loop finishes without a correct guess

### Task 2 – Multiplication Table Generator (For Loop)
- Takes a number from the user
- Uses `for i in range(1, 11)` to print that number's multiplication table from 1 to 10

### Task 3 – BMI Calculator (Function)
- `calculate_bmi(weight, height)` returns `weight / height**2`
- Takes weight (kg) and height (m) from the user and prints the BMI to 2 decimal places

## Sample Output
```
Guess the number (between 1 and 10): 2
Too low. Try again.
Guess the number (between 1 and 10): 15
Your guess is out of range. Please guess a number between 1 and 10.
Guess the number (between 1 and 10): 5
Too high. Try again.
Guess the number (between 1 and 10): 3
Congratulations! You guessed the correct number.

Enter the number for which you want the multiplication table: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

Enter your weight in kg: 58
Enter your height in meters: 1.62
Your BMI is: 22.10
```
*(Guessing game output varies each run since the secret number is random.)*

## How to Run
```bash
python Assignment3.py
```
Play the guessing game first, then enter a number for the multiplication table, then your weight and height for the BMI calculation.

## Skills Demonstrated
- Iterative execution with `while` and `for` loops
- Control statements: `break`, `continue`, `while...else`
- Problem-solving with conditional guess feedback
- Function definition, parameters, and return values
- Input handling and formatted output

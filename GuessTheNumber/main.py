# This is a simple Python program that demonstrates basic input/output, variables, conditional statements, and loops.

# OUTPUT demo
print("Hello, Gail!")

# VARIABLES and INPUT demo
temp = float(input("What is the temperature in Celsius? "))
print ("The temperature in Celsius is: ", temp)
print ("The temperature in Fahrenheit is: ", (temp * 9/5) + 32)

# CONDITIONAL STATEMENT demo
if temp < 0:
    print("It's freezing!")
else:
    print("It's springtime!")

# LOOP demo
answer = "yes"
while( answer == "yes"):
    answer = input("Do you want to continue? (yes/no) ")

# Putting it all together
# INPUT, OUTPUT, VARIABLE, LOOP and CONDITIONAL STATEMENT demo

import random
theNumber = random.randint(1, 10)  # Generate a random number between 1 and 10)
print ("Num is: ", theNumber)
guess = -1

while (guess != theNumber):
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < theNumber:
        print("Too low!")
    if guess > theNumber:
        print("Too high!")
print("Congratulations! You guessed the number.")

# the end
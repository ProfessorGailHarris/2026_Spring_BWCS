# This is a comment line. It is ignored when the program is run.

# Puzzles for Spring 2026 BWCS

# INSTRUCTIONS
# The puzzles are organized into sections. Each section begins with one or two lines like this:
# 
# PUZZLES about XXXX
# HINT: here's some extra information that may help you solve the puzzles in this section.
#
#
# To try each puzzle remove the "#" at the beginning of each statement in a puzzle section.
# Run the project, which will cause error messages.
# Figure out how to fix the code in the section so that no more errors appear when you run the project.
# If you are stuck you should try a few things, and then ask for help if you are still stuck.
# Remember, you can always put the "#" at the front of a line until you can receive help.
# 

# PUZZLES about OUTPUT
# HINT: read the error messages carefully.

#print "My name is long."

#name = "Mr. Hayes"
#print( "My teacher's name is" name)

# PUZZLES about INPUT
# HINT: input is treated as a string by default. You need to do something extra to use numerical input in a calculation.

#temp = input(What is the water temperature? )
#print ("Temp is", temp)

#airTemp = flot(input("what is the air temperature in Celsius? "))
#print("The temp in C is", airTemp, "and the temp in F is", airTemp * 9/5 + 32)

#bodyTempFahrenheit = input("what is your body temperature in Fahrenheit? ")
#bodyTempCelsius = (bodyTempFahrenheit - 32) * 5/9
#print ("Your body temperature is", bodyTempCelsius, "Celsius")

# PUZZLES about VARIABLES
# HINT: explore the rules for variable names. Many computer languages have similar rules.

#age = 14
#print("my age is", AGE)

#?averageAge = 14.5
#average-Age = 13.5

# PUZZLES about IF statements
# HINT: you should mostly change the code on the line with IF (...)

guess = 5

#if (guess > 10):
#  print ("You got this Right!")
#else:
#  print ("Ooops. Fix the 'if' clause.")

#if guess > 1
#  print("You got this right too!")

#if guess = 5:
#  print ("Guess should be 5 still. Value of guess is:", guess)


# BONUS QUESTION: 

#if guess > 5 and guess < 10:
#  print ("Wooooo! I am brilliant.")
#else
#  print ("More work to do")
  

# PUZZLES about LOOPS
max = 8
i = 0

#while (i > max):
#  i = i + 1
#  print ("Count up:", i)
#  if (i == 8):
#    print ("Well done!")

#for i in range(5):
#  print ("Count up using for loop:", i)
#  if (i != 4):
#    print("Good work! This only printed once")

import random
theNumber = random.randint(1, 10)  # Generate a random number between 1 and 10)
guess = -1


# HINT: the clues might be leading you astray

#while (guess != theNumber):
#    guess = int(input("Guess the number between 1 and 10: "))
#    if guess > theNumber:
#        print("Too low!")
#    if guess < theNumber:
#        print("Too high!")
#print("Congratulations! You guessed the number is", theNumber)

import random

#declaring variable for take user input
name = input("Enter your name: ")
print("Welcome to the number guessing game....",   "Mr./Mrs.", name)
range = input("Enter a non zero number: ")

if range.isdigit():
    range = int(range)
else:
    print("Enter the number only...!!")
    quit()

#generating the random number
random_num = random.randint(0, range)
attempt = 0 #variable declaration for counting the attempt

#checking, the value is integer or not
while True:
    attempt += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please..  Enter the Number only.")
        continue

#comparing the guessed number with generated number
    if guess == random_num:
        print("Congrats!!! your guess is correct.")
        break
    elif guess > random_num:
        print("your number is greater.")
    else:
        print("your number is lower.")

print("You guessed the nuber in", attempt, "attempt.")
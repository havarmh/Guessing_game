import random

print("Hello! ")
player_name = input("What is your name? ")
print("Okay, " + player_name + ". I'm thinking of a number between 1 and 10!")

number = random.randint(1, 10)

number_of_guesses = 0

while number_of_guesses < 3:
    number_of_guesses += 1
    guess = int(input())
    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high.")
    if guess == number:
        break

if guess == number:
    print("You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("You didn't guess the number. The number was " + str(number))

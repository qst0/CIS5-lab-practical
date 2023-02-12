import random

print("I'm thinking of a number between 0 and 100...")
x = random.randint(0, 100)
guess = -1
while guess != x:
    guess = input("Guess: ")
    if guess.isdigit():
        guess = int(guess)
    if isinstance(guess, int) == False:
        print("Please only enter integer guesses.")
        exit(0)
    if guess < x:
        print("Guess higher!")
    if guess > x:
        print("Guess lower!")
    if guess == x:
        print("Wow you won!")
        break
    print("I'm still thinking of a number between 0 and 100...")
print(f"How did you know I was thinking of {x}?")
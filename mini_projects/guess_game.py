import random

# function to generate number
def generate_number():
    return random.randint(1, 10)

secret = generate_number()

while True:
    guess = int(input("Guess number (1-10): "))

    if guess == secret:
        print("Correct! You guessed it.")
        break
    elif guess < secret:
        print("Too small")
    else:
        print("Too large")

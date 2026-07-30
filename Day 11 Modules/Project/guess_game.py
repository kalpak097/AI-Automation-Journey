import random

secret = random.randint(1, 20)

while True:
    guess = int(input("Guess (1-20): "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("higher!")
    else:
        print("lower!")
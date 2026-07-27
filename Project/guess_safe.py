secret = 7

while True:
    try:
        guess = int(input("Guess the number: "))

        if guess == secret:
            print("Correct!")
            break
        else:
            print("Try Again!")

    except ValueError:
        print("Please enter a valid number.")
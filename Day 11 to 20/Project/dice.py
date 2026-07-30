import random

while True:
    input("Press Enter to roll the dice...")

    print("You rolled:", random.randint(1, 6))

    again = input("Roll again? (y/n): ").lower()

    if again != "y":
        break
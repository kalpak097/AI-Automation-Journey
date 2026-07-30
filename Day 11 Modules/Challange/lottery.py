import random

# Generate 6 unique random numbers between 1 and 49
lottery_numbers = random.sample(range(1, 50), 6)

# Sort the numbers in ascending order
lottery_numbers.sort()

# Format numbers as space-separated text
formatted_numbers = " ".join(map(str, lottery_numbers))

# Display the output
print("Your Lottery Numbers:")
print(formatted_numbers)
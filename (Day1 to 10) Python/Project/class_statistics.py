marks = []

# Ask for 5 student marks and store them in a list
for i in range(1, 6):
    mark = float(input(f"Enter mark for student {i}: "))
    marks.append(mark)

# Calculate statistics
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\n--- Statistics ---")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Average mark: {average:.2f}")

print("\n--- Student Results ---")
for i, mark in enumerate(marks, start=1):
    status = "Passed" if mark >= 35 else "Failed"
    print(f"Student {i}: {mark} - {status}")
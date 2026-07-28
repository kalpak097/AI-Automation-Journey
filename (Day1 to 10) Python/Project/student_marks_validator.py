marks = []

for i in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter mark for student {i} (0-100): "))
            
            # Check if marks are within the valid range
            if 0 <= mark <= 100:
                marks.append(mark)
                break  # Exit input loop for this student once valid
            else:
                print("Error: Marks must be between 0 and 100. Please try again.")

        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")

# Print statistical summary
print("\n--- Summary ---")
print(f"Highest mark: {max(marks)}")
print(f"Lowest mark: {min(marks)}")
print(f"Average mark: {sum(marks) / len(marks):.2f}")
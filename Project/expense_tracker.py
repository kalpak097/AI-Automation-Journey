# Open file in append mode to store expenses
with open("expenses.txt", "a") as file:
    while True:
        name = input("Expense Name: ")
        if name.lower() == "done":
            break

        amount = input("Amount: ")
        
        # Save to file in the format: Name - Amount
        file.write(f"{name} - {amount}\n")

print("Expenses saved successfully!")

# Read and print the content from expenses.txt
with open("expenses.txt", "r") as file:
    print(file.read().strip())
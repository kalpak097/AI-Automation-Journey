balance = 1000

try:
    withdrawal = float(input("Enter withdrawal amount: "))

    if withdrawal < 0:
        raise ValueError("Withdrawal cannot be negative.")

    if withdrawal <= balance:
        print("Transaction Successful")
        print("Remaining Balance:", balance - withdrawal)
    else:
        print("Insufficient Balance")

except ValueError as error:
    print(error)
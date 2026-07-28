try:
    a = float(input("First number: "))
    b = float(input("Second number: "))

    print("Answer:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")
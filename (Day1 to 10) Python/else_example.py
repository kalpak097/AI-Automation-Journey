try:
    age = int(input("Enter age: "))

except ValueError:
    print("Invalid age.")

else:
    print(f"You are {age} years old.")
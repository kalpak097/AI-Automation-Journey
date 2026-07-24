def c_to_f(c):
    return (c * 9/5) + 32

temp = float(input("Enter Celsius: "))

print(f"Fahrenheit: {c_to_f(temp):.2f}")
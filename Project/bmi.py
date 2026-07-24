def bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

result = bmi(weight, height)

print(f"BMI = {result:.2f}")
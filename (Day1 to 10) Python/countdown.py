import time

number = int(input("Start countdown from: "))

while number > 0:
    print(number)
    time.sleep(1)  # Pauses execution for 1 second
    number -= 1

print("🚀 Blast Off!")
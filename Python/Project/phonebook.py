phonebook = {}

for i in range(3):
    name = input("Name: ")
    number = input("Phone Number: ")

    phonebook[name] = number

print("\nPhone Book")

for name, number in phonebook.items():
    print(f"{name}: {number}")
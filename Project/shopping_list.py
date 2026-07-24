shopping = []

for i in range(50):
    item = input(f"Enter item {i + 1}: ")
    shopping.append(item)

print("\nShopping List")

for item in shopping:
    print("-", item)
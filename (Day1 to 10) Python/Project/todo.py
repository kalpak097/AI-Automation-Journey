tasks = []

while True:
    task = input("Add a task (or type 'done'): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour Tasks")

for task in tasks:
    print("-", task)
entry = input("Today's diary entry: ")

with open("diary.txt", "a") as file:
    file.write(entry + "\n")

print("Diary updated!")
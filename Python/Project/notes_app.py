note = input("Write a note: ")

with open("my_notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved successfully!")
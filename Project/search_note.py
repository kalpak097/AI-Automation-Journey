# Ask the user for a search word
search_word = input("Enter a word to search: ")

try:
    # Open and read my_notes.txt
    with open("my_notes.txt", "r") as file:
        content = file.read()
        
        # Check if the word exists in the file content
        if search_word in content:
            print("Word found!")
        else:
            print("Word not found.")

except FileNotFoundError:
    print("Error: my_notes.txt does not exist. Please create the file first.")
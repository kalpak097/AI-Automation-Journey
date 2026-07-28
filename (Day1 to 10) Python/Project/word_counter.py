sentence = input("Enter a sentence: ")

words = sentence.lower().split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print("\nWord Count")

for word, total in count.items():
    print(f"{word}: {total}")
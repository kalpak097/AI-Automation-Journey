import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(19):
    password += random.choice(characters)

print("Generated Password:")
print(password)
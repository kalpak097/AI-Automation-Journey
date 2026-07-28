def check_password(password):
    if len(password) < 8:
        return "Weak"
    elif 8 <= len(password) <= 11:
        return "Medium"
    else:
        return "Strong"

# Example usage:
user_password = input("Enter a password to check: ")
strength = check_password(user_password)

print(f"Password Strength: {strength}")
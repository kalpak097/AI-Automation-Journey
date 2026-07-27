CORRECT_PASSWORD = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        user_input = input("Enter password: ")
        
        # Ensure user didn't just press Enter / leave it blank
        if not user_input.strip():
            raise ValueError("Password cannot be empty.")

        if user_input == CORRECT_PASSWORD:
            print("Login Successful")
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect password. Attempts remaining: {remaining}")

    except ValueError as e:
        print(f"Error: {e}")

# If loop finishes without a successful break
if attempts == max_attempts:
    print("Account Locked")
user_name = input("Enter your name: ")

# Ensure the username has at least 3 characters
if len(user_name) < 3:
    print(" Name must have at least 3 characters.")
else:
    print(f"Hello {user_name}, How are you?")

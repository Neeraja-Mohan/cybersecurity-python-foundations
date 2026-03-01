# ==========================================
# Conditional Practice 1 - Login Monitor
# ==========================================

username = input("Enter username: ")
failed_attempts = int(input("Enter number of failed login attempts: "))

if failed_attempts == 0:
    print("Login successful.")
elif failed_attempts < 3:
    print("Warning: Multiple failed attempts detected.")
elif failed_attempts < 5:
    print("Account temporarily locked.")
else:
    print("Account permanently locked. Contact administrator.")


# ==========================================
# Conditional Practice 2 - Password Strength
# ==========================================

password = input("Enter a password: ")

if len(password) < 8:
    print("Password too short.")
elif password.islower():
    print("Password should include uppercase letters.")
elif password.isalpha():
    print("Password should include numbers or symbols.")
else:
    print("Password looks strong.")

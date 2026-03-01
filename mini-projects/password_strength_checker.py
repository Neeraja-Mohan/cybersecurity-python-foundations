# ==========================================
# Mini Project: Password Strength Checker
# ==========================================

print("=== Password Strength Checker ===")

password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_symbol = True

if len(password) < 8:
    print("Weak: Password must be at least 8 characters long.")
elif not has_upper:
    print("Weak: Add at least one uppercase letter.")
elif not has_lower:
    print("Weak: Add at least one lowercase letter.")
elif not has_digit:
    print("Weak: Add at least one number.")
elif not has_symbol:
    print("Moderate: Consider adding a special symbol.")
else:
    print("Strong password.")

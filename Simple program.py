import re

def check_password(password):
    score = 0
    suggestions = []

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters")

    # Rule 2: Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z)")

    # Rule 3: Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z)")

    # Rule 4: Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9)")

    # Rule 5: Special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        suggestions.append("Use at least one special character (@, $, %, etc.)")

    # Strength classification
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# -------- MAIN PROGRAM --------
password = input("Enter your password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

if strength != "Strong":
    print("Suggestions to improve your password:")
    for tip in suggestions:
        print("-", tip)
else:
    print("Your password is strong and meets security requirements.")

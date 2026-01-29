import re
import math

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    return score

def cracking_time(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[@$!%*?&]", password):
        charset += 7

    combinations = charset ** len(password)
    seconds = combinations / 1e6  # assume 1 million guesses/sec

    return seconds

password = input("Enter a password: ")
score = password_strength(password)

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

time_to_crack = cracking_time(password)

print("\nPassword Strength:", strength)
print("Estimated cracking time (seconds):", round(time_to_crack, 2))

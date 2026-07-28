import re

def analyze_password(password):

    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return score, feedback


def password_strength(score):

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


password = input("Enter Password: ")

score, feedback = analyze_password(password)

print("\nSecurity Report")
print("-" * 30)
print("Score:", score)
print("Strength:", password_strength(score))

if feedback:
    print("\nRecommendations:")
    for item in feedback:
        print("-", item)
else:
    print("\nExcellent password!")
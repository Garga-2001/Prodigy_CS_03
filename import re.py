import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    strength_levels = {0: "Very Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong", 5: "Excellent"}
    
    return strength_levels[strength], feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for suggestion in feedback:
            print(f"- {suggestion}")

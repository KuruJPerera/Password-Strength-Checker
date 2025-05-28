# password Checker v3.

def check_password_strength(password):
    score = 0

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        score += 1

    # Check if password has a lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
        
    if has_lower:
        score += 1

    # Check if password has an uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
        
    if has_upper:
        score += 1

    # Check if password has a digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1

    # Check if password has a special character
    special_characters = "!@#$%^&*()_+={}[]|:;'<>,.?/~`"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if has_special:
        score += 1

    # Check if the password does not contain the word 'password'
    if 'password' not in password.lower():
        score += 1

    # Print the score and strength
    print("Password Strength Score:", score, "/6")
    
    if score <= 2:
        print("Weak password")
        
    elif score <= 4:
        print("Moderate password")
        
    else:
        print("Strong password")

# Usage
password = input("Enter a password: ")
check_password_strength(password)

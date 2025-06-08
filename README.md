
# Password Strength Checker v3

This Python script evaluates the strength of a user-provided password based on several criteria. It checks for length, character variety, and whether the password avoids using common weak terms. The script then outputs a score and classifies the password as Weak, Moderate, or Strong.

---

## What Does It Check?

The script evaluates passwords based on six key criteria:

1. Minimum length of 8 characters  
2. Contains at least one lowercase letter  
3. Contains at least one uppercase letter  
4. Contains at least one digit  
5. Contains at least one special character (`!@#$%^&*()_+={}[]|:;'<>,.?/~``)  
6. Does not include the word "password"

Each satisfied criterion adds 1 point to the score, for a total of up to 6 points.

---

## Scoring System

- **0–2 points** → Weak password  
- **3–4 points** → Moderate password  
- **5–6 points** → Strong password  

The script prints both the numeric score and a strength label.

---

## Getting Started

### Requirements

- Python 3 installed  
- A terminal or code editor for running the script

If Python isn’t installed, you can download it here:  
https://www.python.org/downloads/

---

## How to Use

1. Save the script to a `.py` file (e.g., `password_checker.py`)  
2. Open a terminal and run the script:  
   ```bash
   python password_checker.py
   ```

3. When prompted, enter a password for evaluation.

---

## Example Output

```
Enter a password: Hello@2024
Password Strength Score: 6 /6
Strong password
```

---

## Notes

- This is a basic checker and does not guarantee password security.
- For real-world applications, consider using password strength libraries like `zxcvbn` or built-in password policies in authentication systems.

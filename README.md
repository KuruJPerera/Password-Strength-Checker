This program is a Python password strength checker that evaluates a given password against six criteria. It calculates a score out of 6 and classifies the password as Weak, Moderate, or Strong based on the score. The check is performed in real time as the user inputs a password.

The program is made up of one Python function: check_password_strength.

Check password strength:

. Checks if the password is at least 8 characters long.
. Verifies presence of at least one lowercase letter.
. Verifies presence of at least one uppercase letter.
. Verifies presence of at least one digit.
. Checks for special characters like !@#$%^&*(), etc.
. Ensures the word "password" is not part of the input.
. Each criterion met adds 1 point to the score. The final score determines the strength category printed to the user.

Usage:

. Run the script and enter a password when prompted.
. The program will evaluate the password and display a score out of 6 along with a strength label (Weak, Moderate, or Strong).

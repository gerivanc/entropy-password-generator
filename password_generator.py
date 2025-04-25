"""
EntroPy Password Generator
=========================
A secure and customizable password generator written in Python.
Features:
- Generates passwords with lengths between 15 and 128 characters.
- Supports uppercase letters, lowercase letters, digits, and special characters.
- Option to exclude ambiguous characters for better readability.
- Calculates password entropy to assess strength.
- Command-line interface for flexible usage.

Author: [Your Name or Handle]
License: MIT
"""

import secrets
import string
import math
import argparse

# Character sets
SPECIAL_CHARS = '!@#$%^&*()_+-=[]{}|;:,.<>?~`\\'
UPPERCASE_LETTERS = string.ascii_uppercase  # A-Z
LOWERCASE_LETTERS = string.ascii_lowercase  # a-z
DIGITS = string.digits  # 0-9

# Ambiguous characters
AMBIG_UPPERCASE = 'ILO'  # I, L, O
AMBIG_LOWERCASE = 'ilo'  # i, l, o
AMBIG_DIGITS = '01'      # 0, 1
AMBIG_SPECIAL = '|`'     # Vertical bar and backtick

def generate_password(
    length=66,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True,
    avoid_ambiguous=True
):
    """
    Generates a secure random password with customizable settings and calculates its entropy.
    
    Parameters:
    length (int): Password length (minimum 15, maximum 128)
    use_uppercase (bool): Include uppercase letters (A-Z)
    use_lowercase (bool): Include lowercase letters (a-z)
    use_digits (bool): Include digits (0-9)
    use_special (bool): Include special characters
    avoid_ambiguous (bool): If True, removes visually ambiguous characters
    
    Returns:
    tuple: (password (str), entropy (float)) - Generated password and its entropy in bits
    
    Raises:
    ValueError: If parameters are invalid or no characters are available
    """
    # Validate length
    if not isinstance(length, int) or length < 15 or length > 128:
        raise ValueError("Password length must be an integer between 15 and 128 characters.")

    # Ensure at least one character type is selected
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected.")

    # Initialize character sets
    uppercase_local = UPPERCASE_LETTERS if use_uppercase else ''
    lowercase_local = LOWERCASE_LETTERS if use_lowercase else ''
    digits_local = DIGITS if use_digits else ''
    special_local = SPECIAL_CHARS if use_special else ''

    # Adjust to avoid ambiguous characters
    if avoid_ambiguous:
        if use_uppercase:
            uppercase_local = ''.join(c for c in uppercase_local if c not in AMBIG_UPPERCASE)
        if use_lowercase:
            lowercase_local = ''.join(c for c in lowercase_local if c not in AMBIG_LOWERCASE)
        if use_digits:
            digits_local = ''.join(c for c in digits_local if c not in AMBIG_DIGITS)
        if use_special:
            special_local = ''.join(c for c in special_local if c not in AMBIG_SPECIAL)

    # Combine available characters
    all_chars = uppercase_local + lowercase_local + digits_local + special_local

    if not all_chars:
        raise ValueError("No characters available to generate the password after configuration.")

    # Determine minimum required characters
    min_required = (
        (1 if use_uppercase else 0) +
        (1 if use_lowercase else 0) +
        (1 if use_digits else 0) +
        (1 if use_special else 0)
    )

    # Ensure length is sufficient for required characters
    if length < min_required:
        raise ValueError(f"Password length must be at least {min_required} to include all selected character types.")

    # Ensure at least one character of each selected type
    password = []
    if use_uppercase:
        password.append(secrets.choice(uppercase_local))
    if use_lowercase:
        password.append(secrets.choice(lowercase_local))
    if use_digits:
        password.append(secrets.choice(digits_local))
    if use_special:
        password.append(secrets.choice(special_local))

    # Fill the remaining length
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_chars))

    # Shuffle the password securely
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    # Calculate entropy
    charset_size = len(set(all_chars))
    entropy = math.log2(charset_size) * length

    return ''.join(password), entropy

def main():
    """
    Command-line interface for the EntroPy Password Generator.
    Allows customization of password generation via terminal arguments.
    """
    parser = argparse.ArgumentParser(
        description="EntroPy Password Generator: A secure and customizable password generator."
    )
    parser.add_argument(
        "--length", type=int, default=66,
        help="Password length (15 to 128 characters, default: 66)"
    )
    parser.add_argument(
        "--no-uppercase", action="store_false", dest="use_uppercase",
        help="Exclude uppercase letters"
    )
    parser.add_argument(
        "--no-lowercase", action="store_false", dest="use_lowercase",
        help="Exclude lowercase letters"
    )
    parser.add_argument(
        "--no-digits", action="store_false", dest="use_digits",
        help="Exclude digits"
    )
    parser.add_argument(
        "--no-special", action="store_false", dest="use_special",
        help="Exclude special characters"
    )
    parser.add_argument(
        "--with-ambiguous", action="store_false", dest="avoid_ambiguous",
        help="Include ambiguous characters"
    )

    args = parser.parse_args()

    try:
        password, entropy = generate_password(
            length=args.length,
            use_uppercase=args.use_uppercase,
            use_lowercase=args.use_lowercase,
            use_digits=args.use_digits,
            use_special=args.use_special,
            avoid_ambiguous=args.avoid_ambiguous
        )
        print(f"Generated password: {password}")
        print(f"Entropy: {entropy:.2f} bits")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        print("\nPassword 01. 15 characters, default, no ambiguous characters, all character types")
        password, entropy = generate_password(length=15, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 02. 18 characters, with ambiguous characters, all character types")
        password, entropy = generate_password(length=18, avoid_ambiguous=False)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 03. 20 characters, only lowercase letters and digits")
        password, entropy = generate_password(length=20, use_uppercase=False, use_special=False)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 04. 20 characters, only uppercase letters and digits")
        password, entropy = generate_password(length=20, use_lowercase=False, use_special=False)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 05. 24 characters, default, no ambiguous characters, all character types")
        password, entropy = generate_password(length=24, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 06. 32 characters, default, no ambiguous characters")
        password, entropy = generate_password(length=32, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 07. 42 characters, default, no ambiguous characters")
        password, entropy = generate_password(length=42, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 08. 60 characters, default, no ambiguous characters")
        password, entropy = generate_password(length=60, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 09. 75 characters, default, no ambiguous characters")
        password, entropy = generate_password(length=75, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

        print("\nPassword 10. Maximum 128 characters, all character types")
        password, entropy = generate_password(length=128, avoid_ambiguous=True)
        print(f"Password: {password}")
        print(f"Entropy: {entropy:.2f} bits")

    except ValueError as e:
        print(f"Error: {e}")
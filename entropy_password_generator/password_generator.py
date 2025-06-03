"""
EntroPy Password Generator - A secure and customizable password generator
written in Python.

This script provides a command-line interface for generating strong, random
passwords with customizable character sets and calculates their entropy to
assess strength. It includes 20 predefined modes for password generation,
ensuring high security standards.

=========================
Features:
- Generates passwords with lengths between 15 and 128 characters.
- Supports uppercase letters, lowercase letters, digits, and special
  characters.
- Option to exclude ambiguous characters for better readability.
- Calculates password entropy to assess strength.
- Command-line interface for flexible usage.
----------------------------------------

Copyright © 2025 Gerivan Costa dos Santos
EntroPy Password Generator
Author: gerivanc
GitHub: https://github.com/gerivanc
MIT License:
https://github.com/gerivanc/entropy-password-generator/blob/main/LICENSE.md
Changelog:
https://github.com/gerivanc/entropy-password-generator/blob/main/CHANGELOG.md
Issue Report:
https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md
Version: 0.6.0
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

# Define configurations for all 20 modes
MODES = {
    # Block I: All with ambiguous characters, length 24
    1: {"length": 24, "use_uppercase": False, "use_lowercase": True,
        "use_digits": False, "use_special": True, "avoid_ambiguous": False},
    2: {"length": 24, "use_uppercase": True, "use_lowercase": False,
        "use_digits": False, "use_special": True, "avoid_ambiguous": False},
    3: {"length": 24, "use_uppercase": True, "use_lowercase": True,
        "use_digits": False, "use_special": False, "avoid_ambiguous": False},
    4: {"length": 24, "use_uppercase": True, "use_lowercase": False,
        "use_digits": True, "use_special": False, "avoid_ambiguous": False},
    5: {"length": 24, "use_uppercase": False, "use_lowercase": True,
        "use_digits": True, "use_special": False, "avoid_ambiguous": False},
    6: {"length": 24, "use_uppercase": False, "use_lowercase": False,
        "use_digits": True, "use_special": True, "avoid_ambiguous": False},
    7: {"length": 24, "use_uppercase": True, "use_lowercase": True,
        "use_digits": True, "use_special": False, "avoid_ambiguous": False},
    8: {"length": 24, "use_uppercase": True, "use_lowercase": True,
        "use_digits": False, "use_special": True, "avoid_ambiguous": False},
    9: {"length": 24, "use_uppercase": True, "use_lowercase": False,
        "use_digits": True, "use_special": True, "avoid_ambiguous": False},
    10: {"length": 24, "use_uppercase": False, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": False},
    # Block II: Mixed configurations
    11: {"length": 15, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
    12: {"length": 18, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": False},
    13: {"length": 20, "use_uppercase": False, "use_lowercase": True,
         "use_digits": True, "use_special": False, "avoid_ambiguous": True},
    14: {"length": 20, "use_uppercase": True, "use_lowercase": False,
         "use_digits": True, "use_special": False, "avoid_ambiguous": True},
    15: {"length": 24, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
    16: {"length": 32, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
    17: {"length": 42, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
    18: {"length": 60, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
    19: {"length": 75, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
    20: {"length": 128, "use_uppercase": True, "use_lowercase": True,
         "use_digits": True, "use_special": True, "avoid_ambiguous": True},
}


def print_header():
    """
    Prints the header with project information at the start of the script
    execution.
    """
    header = (
        "Copyright © 2025 Gerivan Costa dos Santos\n"
        "EntroPy Password Generator\n"
        "Author: gerivanc\n"
        "GitHub: https://github.com/gerivanc\n"
        "MIT License: https://github.com/gerivanc/entropy-password-"
        "generator/blob/main/LICENSE.md\n"
        "Changelog: https://github.com/gerivanc/entropy-password-"
        "generator/blob/main/CHANGELOG.md\n"
        "Issue Report: https://github.com/gerivanc/entropy-password-"
        "generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md\n"
        "Version: 0.6.0\n"
        "----------------------------------------\n"
    )
    print(header)


def generate_password(
    length=72,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True,
    avoid_ambiguous=True
):
    """
    Generates a secure random password with customizable settings and
    calculates its entropy.

    Parameters:
    length (int): Password length (minimum 15, maximum 128)
    use_uppercase (bool): Include uppercase letters (A-Z)
    use_lowercase (bool): Include lowercase letters (a-z)
    use_digits (bool): Include digits (0-9)
    use_special (bool): Include special characters
    avoid_ambiguous (bool): If True, removes visually ambiguous characters

    Returns:
    tuple: (password (str), entropy (float)) - Generated password and its
           entropy in bits

    Raises:
    ValueError: If parameters are invalid or no characters are available
    """
    # Validate length
    if not isinstance(length, int) or length < 15 or length > 128:
        raise ValueError("Password length must be an integer between 15 and "
                         "128 characters.")

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
            uppercase_local = ''.join(c for c in uppercase_local
                                      if c not in AMBIG_UPPERCASE)
        if use_lowercase:
            lowercase_local = ''.join(c for c in lowercase_local
                                      if c not in AMBIG_LOWERCASE)
        if use_digits:
            digits_local = ''.join(c for c in digits_local
                                   if c not in AMBIG_DIGITS)
        if use_special:
            special_local = ''.join(c for c in special_local
                                    if c not in AMBIG_SPECIAL)

    # Combine available characters
    all_chars = uppercase_local + lowercase_local
    all_chars += digits_local + special_local

    if not all_chars:
        raise ValueError("No characters available to generate the password "
                         "after configuration.")

    # Determine minimum required characters
    min_required = (1 if use_uppercase else 0) + \
                   (1 if use_lowercase else 0) + \
                   (1 if use_digits else 0) + \
                   (1 if use_special else 0)

    # Ensure length is sufficient for required characters
    if length < min_required:
        raise ValueError("Password length must be at least "
                         f"{min_required} to include all selected "
                         "character types.")

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

    # Warn if entropy is below the Proton© recommended minimum (75 bits)
    if entropy < 75:
        suggestions = []
        if length < 24:
            suggestions.append("increase the password length (e.g., use "
                               "--length 24 or higher)")
        if sum([use_uppercase, use_lowercase, use_digits, use_special]) < 3:
            suggestions.append("include more character types (e.g., use "
                               "uppercase, lowercase, digits, and special "
                               "characters)")
        if suggestions:
            suggestion_text = " and ".join(suggestions)
        else:
            suggestion_text = "use a stronger configuration"
        print("----------------------------------------")
        print("Warning: Password entropy ({entropy:.2f} bits) is below the "
              "recommended 75 bits (Proton© standard).")
        print(f"To improve security, {suggestion_text}.")
        print("----------------------------------------")

    return ''.join(password), entropy


def main():
    """
    Command-line interface for the EntroPy Password Generator.
    Allows customization of password generation via terminal arguments.
    """
    parser = argparse.ArgumentParser(
        description="EntroPy Password Generator: A secure and customizable "
                    "password generator."
    )
    parser.add_argument(
        "--mode", type=int, choices=range(1, 21),
        help="Password generation mode (1 to 20, corresponding to predefined "
             "configurations)"
    )
    parser.add_argument(
        "--length", type=int, default=72,
        help="Password length (15 to 128 characters, default: 72). Ignored "
             "if --mode is specified."
    )
    parser.add_argument(
        "--no-uppercase", action="store_false", dest="use_uppercase",
        help="Exclude uppercase letters. Ignored if --mode is specified."
    )
    parser.add_argument(
        "--no-lowercase", action="store_false", dest="use_lowercase",
        help="Exclude lowercase letters. Ignored if --mode is specified."
    )
    parser.add_argument(
        "--no-digits", action="store_false", dest="use_digits",
        help="Exclude digits. Ignored if --mode is specified."
    )
    parser.add_argument(
        "--no-special", action="store_false", dest="use_special",
        help="Exclude special characters. Ignored if --mode is specified."
    )
    parser.add_argument(
        "--with-ambiguous", action="store_false", dest="avoid_ambiguous",
        help="Include ambiguous characters. Ignored if --mode is specified."
    )

    args = parser.parse_args()

    print_header()

    try:
        if args.mode:
            # Mode-based generation
            if args.mode not in MODES:
                raise ValueError(f"Invalid mode: {args.mode}. Must be between "
                                 "1 and 20.")
            config = MODES[args.mode]
            password, entropy = generate_password(
                length=config["length"],
                use_uppercase=config["use_uppercase"],
                use_lowercase=config["use_lowercase"],
                use_digits=config["use_digits"],
                use_special=config["use_special"],
                avoid_ambiguous=config["avoid_ambiguous"]
            )
            print(f"Mode {args.mode} Password:")
            print()
            print(f"Password: {password}")
            print()
            print(f"Length: {len(password)} characters")
            print(f"Entropy: {entropy:.2f} bits")
        else:
            # Custom generation
            password, entropy = generate_password(
                length=args.length,
                use_uppercase=args.use_uppercase,
                use_lowercase=args.use_lowercase,
                use_digits=args.use_digits,
                use_special=args.use_special,
                avoid_ambiguous=args.avoid_ambiguous
            )
            print("Custom Password:")
            print()
            print(f"Password: {password}")
            print()
            print(f"Length: {len(password)} characters")
            print(f"Entropy: {entropy:.2f} bits")
    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

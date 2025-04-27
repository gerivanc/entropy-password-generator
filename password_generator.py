"""
EntroPy Password Generator - A secure and customizable password generator written in Python.

This script provides a command-line interface for generating strong, random passwords with customizable character sets
and calculates their entropy to assess strength. It includes 20 predefined modes for password generation, ensuring high
security standards.

=========================
Features:
- Generates passwords with lengths between 15 and 128 characters.
- Supports uppercase letters, lowercase letters, digits, and special characters.
- Option to exclude ambiguous characters for better readability.
- Calculates password entropy to assess strength.
- Command-line interface for flexible usage.
----------------------------------------

Copyright © 2025 Gerivan Costa dos Santos
EntroPy Password Generator
Author: gerivanc
GitHub: https://github.com/gerivanc
MIT License: https://github.com/gerivanc/entropy-password-generator/blob/main/LICENSE.md
Changelog: https://github.com/gerivanc/entropy-password-generator/blob/main/CHANGELOG.md
Version: 0.3.0
"""

import argparse
import secrets
import math
import string


def build_character_set(use_uppercase=True, use_lowercase=True, use_digits=True,
                       use_special=True, avoid_ambiguous=False):
    """Build the character set based on user preferences."""
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?~\\`"

    if avoid_ambiguous:
        ambiguous_chars = "IlO0"
        for char in ambiguous_chars:
            characters = characters.replace(char, "")

    if not characters:
        raise ValueError("At least one character set must be selected.")

    return characters


def calculate_entropy(length, charset_size):
    """Calculate the entropy of a password in bits."""
    return length * math.log2(charset_size)


def generate_password(length, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_special=True, avoid_ambiguous=False):
    """Generate a secure password with the specified length and character sets."""
    characters = build_character_set(
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_digits=use_digits,
        use_special=use_special,
        avoid_ambiguous=avoid_ambiguous
    )

    password = "".join(secrets.choice(characters) for _ in range(length))
    entropy = calculate_entropy(length, len(characters))
    return password, entropy


def main():
    """Main function to run the password generator from the CLI."""
    parser = argparse.ArgumentParser(description="EntroPy Password Generator")
    parser.add_argument(
        "--length",
        type=int,
        required=True,
        help="Length of the password (15 to 128)"
    )
    parser.add_argument(
        "--no-uppercase",
        action="store_false",
        help="Exclude uppercase letters"
    )
    parser.add_argument(
        "--no-lowercase",
        action="store_false",
        help="Exclude lowercase letters"
    )
    parser.add_argument(
        "--no-digits",
        action="store_false",
        help="Exclude digits"
    )
    parser.add_argument(
        "--no-special",
        action="store_false",
        help="Exclude special characters"
    )
    parser.add_argument(
        "--with-ambiguous",
        action="store_true",
        help="Include ambiguous characters"
    )

    args = parser.parse_args()

    # Ensure length is within acceptable range
    if not (15 <= args.length <= 128):
        raise ValueError("Password length must be between 15 and 128 characters.")

    password, entropy = generate_password(
        length=args.length,
        use_uppercase=args.no_uppercase,
        use_lowercase=args.no_lowercase,
        use_digits=args.no_digits,
        use_special=args.no_special,
        avoid_ambiguous=not args.with_ambiguous
    )

    print(f"Generated password: {password}")
    print(f"Entropy: {entropy:.2f} bits")


if __name__ == "__main__":
    main()

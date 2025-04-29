import argparse
import math
import secrets
import string

def calculate_entropy(length, char_set_size):
    """Calculate the entropy of a password in bits."""
    return math.log2(char_set_size ** length)

def generate_password(length, uppercase=True, lowercase=True, digits=True, special=True, ambiguous=True):
    """Generate a password based on the specified character sets."""
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~\\"
    
    # Remove ambiguous characters if not allowed
    ambiguous_chars = set("IL1O0")
    if not ambiguous:
        uppercase_chars = "".join(c for c in uppercase_chars if c not in ambiguous_chars)
        lowercase_chars = "".join(c for c in lowercase_chars if c not in ambiguous_chars)
        digit_chars = "".join(c for c in digit_chars if c not in ambiguous_chars)
    
    # Build the character pool based on arguments
    char_pool = ""
    if uppercase:
        char_pool += uppercase_chars
    if lowercase:
        char_pool += lowercase_chars
    if digits:
        char_pool += digit_chars
    if special:
        char_pool += special_chars
    
    if not char_pool:
        raise ValueError("At least one character set must be selected (uppercase, lowercase, digits, or special).")
    
    # Generate the password
    password = "".join(secrets.choice(char_pool) for _ in range(length))
    
    # Calculate entropy
    entropy = calculate_entropy(length, len(char_pool))
    
    return password, entropy

def map_arguments_to_mode(args):
    """Map CLI arguments to the corresponding mode and configuration."""
    length = args.length
    uppercase = not args.no_uppercase
    lowercase = not args.no_lowercase
    digits = not args.no_digits
    special = not args.no_special
    ambiguous = args.with_ambiguous
    
    # Define the modes as per README.md, including descriptions
    modes = [
        # Block I: All with ambiguous characters, length 24
        {"mode": 1, "description": "Lowercase + Special characters, with ambiguous characters (length 24)", "length": 24, "uppercase": False, "lowercase": True, "digits": False, "special": True, "ambiguous": True},
        {"mode": 2, "description": "Uppercase + Special characters, with ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": False, "digits": False, "special": True, "ambiguous": True},
        {"mode": 3, "description": "Uppercase + Lowercase, with ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": True, "digits": False, "special": False, "ambiguous": True},
        {"mode": 4, "description": "Uppercase + Digits, with ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": False, "digits": True, "special": False, "ambiguous": True},
        {"mode": 5, "description": "Lowercase + Digits, with ambiguous characters (length 24)", "length": 24, "uppercase": False, "lowercase": True, "digits": True, "special": False, "ambiguous": True},
        {"mode": 6, "description": "Digits + Special characters, with ambiguous characters (length 24)", "length": 24, "uppercase": False, "lowercase": False, "digits": True, "special": True, "ambiguous": True},
        {"mode": 7, "description": "Uppercase + Lowercase + Digits, with ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": True, "digits": True, "special": False, "ambiguous": True},
        {"mode": 8, "description": "Uppercase + Lowercase + Special characters, with ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": True, "digits": False, "special": True, "ambiguous": True},
        {"mode": 9, "description": "Uppercase + Digits + Special characters, with ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": False, "digits": True, "special": True, "ambiguous": True},
        {"mode": 10, "description": "Lowercase + Digits + Special characters, with ambiguous characters (length 24)", "length": 24, "uppercase": False, "lowercase": True, "digits": True, "special": True, "ambiguous": True},
        # Block II: Mixed configurations
        {"mode": 11, "description": "All character types, no ambiguous characters (length 15)", "length": 15, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
        {"mode": 12, "description": "All character types, with ambiguous characters (length 18)", "length": 18, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": True},
        {"mode": 13, "description": "Lowercase + Digits, no ambiguous characters (length 20)", "length": 20, "uppercase": False, "lowercase": True, "digits": True, "special": False, "ambiguous": False},
        {"mode": 14, "description": "Uppercase + Digits, no ambiguous characters (length 20)", "length": 20, "uppercase": True, "lowercase": False, "digits": True, "special": False, "ambiguous": False},
        {"mode": 15, "description": "All character types, no ambiguous characters (length 24)", "length": 24, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
        {"mode": 16, "description": "All character types, no ambiguous characters (length 32)", "length": 32, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
        {"mode": 17, "description": "All character types, no ambiguous characters (length 42)", "length": 42, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
        {"mode": 18, "description": "All character types, no ambiguous characters (length 60)", "length": 60, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
        {"mode": 19, "description": "All character types, no ambiguous characters (length 75)", "length": 75, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
        {"mode": 20, "description": "All character types, no ambiguous characters (length 128)", "length": 128, "uppercase": True, "lowercase": True, "digits": True, "special": True, "ambiguous": False},
    ]
    
    # Find the matching mode
    for mode_config in modes:
        if (mode_config["length"] == length and
            mode_config["uppercase"] == uppercase and
            mode_config["lowercase"] == lowercase and
            mode_config["digits"] == digits and
            mode_config["special"] == special and
            mode_config["ambiguous"] == ambiguous):
            return mode_config["mode"], mode_config
    
    # If no exact match, provide a helpful error message
    error_msg = (
        f"No mode matches the provided arguments: length={length}, uppercase={uppercase}, "
        f"lowercase={lowercase}, digits={digits}, special={special}, ambiguous={ambiguous}\n"
        "Suggestions:\n"
        "- For Block I modes, use --length 24 and enable --with-ambiguous (e.g., --length 24 --no-uppercase --no-digits)\n"
        "- For Block II modes, use lengths like 15, 18, 20, 24, 32, 42, 60, 75, or 128 (e.g., --length 20 --no-lowercase --no-special)\n"
        "- Ensure at least one character set is enabled (avoid using all --no-* options simultaneously)"
    )
    raise ValueError(error_msg)

def main():
    parser = argparse.ArgumentParser(description="EntroPy Password Generator - Generate secure passwords with high entropy.")
    parser.add_argument("--length", type=int, default=72, help="Password length (default: 72)")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")
    parser.add_argument("--with-ambiguous", action="store_true", help="Include ambiguous characters")
    
    args = parser.parse_args()
    
    # Map arguments to a specific mode
    mode, config = map_arguments_to_mode(args)
    
    # Generate the password for the matched mode
    password, entropy = generate_password(
        length=config["length"],
        uppercase=config["uppercase"],
        lowercase=config["lowercase"],
        digits=config["digits"],
        special=config["special"],
        ambiguous=config["ambiguous"]
    )
    
    # Display the result with mode description
    print(f"\nMode {mode}: {config['description']}")
    print(f"Generated password: {password}")
    print(f"Entropy: {entropy:.2f} bits")
    
    # Check for minimum entropy (Proton© standard: 75 bits)
    if entropy < 75:
        print("Warning: Password entropy is below the Proton© recommended minimum of 75 bits.")
        print("Suggestions to improve security:")
        print("- Increase the password length (e.g., use --length 24 or higher)")
        print("- Include more character types (e.g., avoid --no-uppercase, --no-digits, etc.)")

if __name__ == "__main__":
    print("EntroPy Password Generator")
    print("Author: Gerivan Costa dos Santos")
    print("GitHub: https://github.com/gerivanc/entropy-password-generator")
    print("License: https://github.com/gerivanc/entropy-password-generator/blob/main/LICENSE.md")
    print("Changelog: https://github.com/gerivanc/entropy-password-generator/blob/main/CHANGELOG.md")
    print("Version: 0.4.2\n")
    main()

EntroPy Password Generator
EntroPy Password Generator is a secure and customizable password generator written in Python. It creates strong passwords with configurable character sets and calculates their entropy to assess strength. The project provides 20 modes for generating strong passwords, ranging from 15 to 128 characters, with entropies from 95.10 bits to 811.50 bits, exceeding the NIST recommendation of at least 75 bits of entropy. With a command-line interface, it is ideal for developers, security enthusiasts, and anyone needing robust passwords.
Features

Generates passwords with lengths between 15 and 128 characters.
Supports uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and special characters (!@#$%^&*()_+-=[]{}|;:,.<>?~\\\).
Option to exclude visually ambiguous characters (e.g., 'I', 'l', 'O', '0') for better readability.
Calculates password entropy (in bits) to evaluate strength.
Command-line interface (CLI) for flexible usage.
Uses Python's secrets module for cryptographically secure random generation.

Installation

Ensure you have Python 3.6 or higher installed.
Clone the repository:git clone https://github.com/gerivanc/entropy-password-generator.git
cd entropy-password-generator


No additional dependencies are required, as the project uses only Python standard libraries.

Usage
Run the generator via the command-line interface:
python password_generator.py --length 20

CLI Options

--length <length>: Set password length (15 to 128, default: 66).
--no-uppercase: Exclude uppercase letters.
--no-lowercase: Exclude lowercase letters.
--no-digits: Exclude digits.
--no-special: Exclude special characters.
--with-ambiguous: Include ambiguous characters.

Example Password Modes
The project includes 20 predefined password generation modes, divided into two blocks:
Strong Passwords Block I (All with ambiguous characters, length 24):

Lowercase + Special characters.
Uppercase + Special characters.
Uppercase + Lowercase.
Uppercase + Digits.
Lowercase + Digits.
Digits + Special characters.
Uppercase + Lowercase + Digits.
Uppercase + Lowercase + Special characters.
Uppercase + Digits + Special characters.
Lowercase + Digits + Special characters.

Strong Passwords Block II (Mixed configurations):

15 characters, all character types, no ambiguous characters (95.10 bits entropy).
18 characters, all character types, with ambiguous characters.
20 characters, only lowercase letters and digits, no ambiguous characters.
20 characters, only uppercase letters and digits, no ambiguous characters.
24 characters, all character types, no ambiguous characters.
32 characters, all character types, no ambiguous characters.
42 characters, all character types, no ambiguous characters.
60 characters, all character types, no ambiguous characters.
75 characters, all character types, no ambiguous characters.
128 characters, all character types, no ambiguous characters (811.50 bits entropy).

These modes produce passwords with entropies exceeding the NIST recommendation of 75 bits, ensuring high security.
Example CLI Usage
Generate a 20-character password with all character types, excluding ambiguous characters:
python password_generator.py --length 20

Output:
Generated password: K7mPq9xT2rZwYvN5jH
Entropy: 119.42 bits

Generate a 15-character password with only lowercase letters and digits:
python password_generator.py --length 15 --no-uppercase --no-special

Output:
Generated password: kxw9m4p7q2n8r5t
Entropy: 85.75 bits

Entropy Calculation
The generator calculates password entropy using the formula:[\text{Entropy} = \log_2(N) \times L]where (N) is the size of the character set, and (L) is the password length. Higher entropy indicates a stronger password. The project's 20 modes ensure entropies from 95.10 bits (15 characters) to 811.50 bits (128 characters), surpassing the NIST minimum of 75 bits.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
ContributingContributions are welcome! Please open an issue or submit a pull request with your suggestions or improvements.
Contact
For questions or feedback, please contact: enc28ysi@protonmail.com.

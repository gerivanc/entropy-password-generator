# EntroPy Password Generator

**EntroPy Password Generator** is a secure and customizable password generator written in Python. It creates strong passwords with configurable character sets and calculates their entropy to assess strength. With a command-line interface, it is ideal for developers, security enthusiasts, and anyone needing robust passwords.

## Features
- Generates passwords with lengths between 15 and 128 characters.
- Supports uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and special characters (`!@#$%^&*()_+-=[]{}|;:,.<>?~\\\`).
- Option to exclude visually ambiguous characters (e.g., 'I', 'l', 'O', '0') for better readability.
- Calculates password entropy (in bits) to evaluate strength.
- Command-line interface (CLI) for flexible usage.
- Uses Python's `secrets` module for cryptographically secure random generation.

## Installation
1. Ensure you have Python 3.6 or higher installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/entropy-password-generator.git
   cd entropy-password-generator
   ```
3. No additional dependencies are required, as the project uses only Python standard libraries.

## Usage
Run the generator via the command-line interface:

```bash
python password_generator.py --length 20
```

### CLI Options
- `--length <length>`: Set password length (15 to 128, default: 66).
- `--no-uppercase`: Exclude uppercase letters.
- `--no-lowercase`: Exclude lowercase letters.
- `--no-digits`: Exclude digits.
- `--no-special`: Exclude special characters.
- `--with-ambiguous`: Include ambiguous characters.

### Examples
1. Generate a 20-character password with all character types, excluding ambiguous characters:
   ```bash
   python password_generator.py --length 20
   ```
   Output:
   ```
   Generated password: K7mPq9xT2rZwYvN5jH
   Entropy: 119.42 bits
   ```

2. Generate a 15-character password with only lowercase letters and digits:
   ```bash
   python password_generator.py --length 15 --no-uppercase --no-special
   ```
   Output:
   ```
   Generated password: kxw9m4p7q2n8r5t
   Entropy: 85.75 bits
   ```

## Entropy Calculation
The generator calculates password entropy using the formula:

\[
\text{Entropy} = \log_2(N) \times L
\]

where \(N\) is the size of the character set, and \(L\) is the password length. Higher entropy indicates a stronger password.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your suggestions or improvements.

## Contact
For questions or feedback, please contact [your-email or handle].
# internal_tests.py
from entropy_password_generator.password_generator import generate_password, print_header

def run_internal_tests():
    print_header()

    configurations = [
        # Block I
        ("Password 01", 24, False, True, False, True, False),
        ("Password 02", 24, True, False, False, True, False),
        ("Password 03", 24, True, True, False, False, False),
        ("Password 04", 24, True, False, True, False, False),
        ("Password 05", 24, False, True, True, False, False),
        ("Password 06", 24, False, False, True, True, False),
        ("Password 07", 24, True, True, True, False, False),
        ("Password 08", 24, True, True, False, True, False),
        ("Password 09", 24, True, False, True, True, False),
        ("Password 10", 24, False, True, True, True, False),

        # Block II
        ("Password 11", 15, True, True, True, True, True),
        ("Password 12", 18, True, True, True, True, False),
        ("Password 13", 20, False, True, True, False, True),
        ("Password 14", 20, True, False, True, False, True),
        ("Password 15", 24, True, True, True, True, True),
        ("Password 16", 32, True, True, True, True, True),
        ("Password 17", 42, True, True, True, True, True),
        ("Password 18", 60, True, True, True, True, True),
        ("Password 19", 75, True, True, True, True, True),
        ("Password 20", 128, True, True, True, True, True),
    ]

    for label, length, up, low, dig, spec, no_amb in configurations:
        print(f"\n{label}. {length} characters, config: up={up}, low={low}, dig={dig}, spec={spec}, ambiguous={not no_amb}")
        try:
            password, entropy = generate_password(
                length=length,
                use_uppercase=up,
                use_lowercase=low,
                use_digits=dig,
                use_special=spec,
                avoid_ambiguous=no_amb
            )
            print(f"Password: {password}")
            print(f"Entropy: {entropy:.2f} bits")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_internal_tests()

__version__ = "0.6.0"

__all__ = ["generate_password", "main"]

from .password_generator import generate_password, main

"""
EntroPy Password Generator package.

This package provides a secure password generator with configurable character
sets and entropy calculation, supporting 20 predefined modes for generating
strong passwords compliant with Proton© and NIST standards. It includes a
command-line interface (CLI) and a programmable API via the `generate_password`
function.

Example:
    >>> from entropy_password_generator import generate_password
    >>> password, entropy = generate_password(
    ...     length=24, use_special=True
    ... )
    >>> print(
    ...     f"Password: {password}, Entropy: {entropy:.2f} bits"
    ... )

Author: Gerivan Costa dos Santos
License: MIT License
Homepage: https://github.com/gerivanc/entropy-password-generator
PyPI: https://pypi.org/project/entropy-password-generator/
"""

__author__ = "Gerivan Costa dos Santos"
__license__ = "MIT License"
__copyright__ = "Copyright © 2025 Gerivan Costa dos Santos"

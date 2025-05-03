"""EntroPy Password Generator package.

This package provides a secure password generator with configurable character sets
and entropy calculation, supporting 20 predefined modes.
"""

__version__ = "0.4.9"
from .password_generator import generate_password
__all__ = ["generate_password"]

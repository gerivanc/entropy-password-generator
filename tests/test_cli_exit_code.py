"""CLI exit-code tests for the EntroPy Password Generator."""

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "entropy_password_generator" / "password_generator.py"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
    )


class ExitCodeTestCase(unittest.TestCase):
    def test_invalid_length_exits_nonzero(self):
        # An invalid --length must report the error AND exit nonzero so
        # scripts can detect the failure.
        result = run_cli("--length", "5")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Error:", result.stdout)

    def test_no_character_types_exits_nonzero(self):
        result = run_cli(
            "--no-uppercase", "--no-lowercase", "--no-digits", "--no-special"
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Error:", result.stdout)

    def test_valid_run_exits_zero(self):
        result = run_cli("--length", "20")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Password:", result.stdout)


if __name__ == "__main__":
    unittest.main()

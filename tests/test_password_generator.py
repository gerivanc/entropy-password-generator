import pytest
from entropy_password_generator import generate_password

def test_mode_1():
    password, entropy = generate_password(mode=1)
    assert len(password) == 24
    assert 138 <= entropy <= 139
    assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    assert any(c.islower() for c in password)

def test_mode_12():
    password, entropy = generate_password(mode=12)
    assert len(password) == 18
    assert 117 <= entropy <= 119
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

def test_mode_15():
    password, entropy = generate_password(mode=15)
    assert len(password) == 24
    assert 155 <= entropy <= 157
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

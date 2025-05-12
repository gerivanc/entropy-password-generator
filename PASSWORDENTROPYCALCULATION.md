# Password Entropy Calculation
![Badge: Entropy Compliant](https://img.shields.io/badge/Entropy%20Compliant-Proton%C2%A9%20%26%20NIST-brightgreen)

---

## Overview

The **EntroPy Password Generator** creates passwords with high entropy to maximize resistance against brute-force attacks. Entropy measures password strength, indicating the computational effort required to guess a password. All 20 generation modes produce passwords exceeding the Proton© (75 bits) and NIST (80+ bits) recommendations, ensuring robust security for applications ranging from personal accounts to cryptographic keys.

---

## How Entropy is Calculated

The generator uses the standard entropy formula:

\[ E(R) = \log_2(R^L) \]

where:
- **R**: Number of possible characters (character set size).
- **L**: Password length.
- **E(R)**: Entropy in bits.

Simplified:
- Entropy = \(\log_2(\text{charset size}) \times \text{password length}\)
- Higher entropy means exponentially greater effort to crack the password.

> **Note**: Entropy values are theoretical maximums, assuming uniform random selection via Python's `secrets` module. The requirement of at least one character per selected type (e.g., uppercase, lowercase) slightly reduces effective entropy for shorter passwords (e.g., 15 characters). This reduction is negligible for the lengths used (15–128 characters), and all modes exceed Proton© and NIST standards.

To validate entropy locally, run a mode and check the output:
```bash
python3 entropy_password_generator/password_generator.py --mode 1
```

---

## Security Benchmarks

| Source | Minimum Recommended Entropy | Context |
|:------|:-----------------------------|:--------|
| **Proton©** | 75 bits | General password strength ([source](https://proton.me/blog/what-is-password-entropy)) |
| **NIST (SP 800-63B)** | 80+ bits | Passwords protecting sensitive data ([source](https://pages.nist.gov/800-63-3/sp800-63b.html)) |

> **Note**: For highly sensitive accounts (e.g., financial, administrative), aim for **100+ bits** of entropy.

---

## Project Capabilities

### Password Generation Modes
The generator offers 20+ modes for secure password generation, divided into three blocks:

- **Block I (Modes 1–10)**: Fixed length (24 characters), includes ambiguous characters (e.g., `I`, `l`, `O`, `0`), balancing readability and security. Ideal for general-purpose passwords.
- **Block II (Modes 11–20)**: Varying lengths (15–128 characters), mostly excluding ambiguous characters (`I`, `l`, `O`, `0`, `1`, `` ` ``). Suitable for sensitive applications.
- **Block III (Using Custom Configuration)**: Lengths from 15–128 characters, with or without ambiguous characters, using `--length` and `--with-ambiguous`.

The table below details each mode, with character set sizes (\( R \)), entropy, and use cases. Ambiguous characters are excluded unless specified.

| Mode | Password Length | Character Set | R (Charset Size) | Entropy (bits) | Security Level | Use Case |
|------|-----------------|---------------|------------------|----------------|----------------|----------|
| 11 | 15 | Full (no ambiguous) | 94 | 95.10 | Strong | Personal accounts |
| 13 | 20 | Lowercase + Digits (no ambiguous) | 36 | 99.08 | Strong | Basic logins |
| 14 | 20 | Uppercase + Digits (no ambiguous) | 36 | 99.08 | Strong | Device authentication |
| 12 | 18 | Full (with ambiguous) | 95 | 117.14 | Very Strong | Professional accounts |
| 4 | 24 | Uppercase + Digits (with ambiguous) | 36 | 124.08 | Very Strong | Legacy systems |
| 5 | 24 | Lowercase + Digits (with ambiguous) | 36 | 124.08 | Very Strong | Readable passwords |
| 6 | 24 | Digits + Special (with ambiguous) | 43 | 126.85 | Very Strong | API tokens |
| 3 | 24 | Uppercase + Lowercase (with ambiguous) | 52 | 136.81 | Very Strong | Website logins |
| 1 | 24 | Lowercase + Special (with ambiguous) | 59 | 138.75 | Very Strong | Secure notes |
| 2 | 24 | Uppercase + Special (with ambiguous) | 59 | 138.75 | Very Strong | Admin access |
| 7 | 24 | Uppercase + Lowercase + Digits (with ambiguous) | 62 | 142.90 | Very Strong | System credentials |
| 9 | 24 | Uppercase + Digits + Special (with ambiguous) | 69 | 144.54 | Very Strong | Database keys |
| 10 | 24 | Lowercase + Digits + Special (with ambiguous) | 69 | 144.54 | Very Strong | File encryption |
| 8 | 24 | Uppercase + Lowercase + Special (with ambiguous) | 85 | 151.16 | Extremely Strong | High-security logins |
| 15 | 24 | Full (no ambiguous) | 94 | 152.16 | Extremely Strong | Enterprise passwords |
| 16 | 32 | Full (no ambiguous) | 94 | 202.88 | Cryptographic Grade | API keys |
| 17 | 42 | Full (no ambiguous) | 94 | 266.27 | Cryptographic Grade | Server tokens |
| 18 | 60 | Full (no ambiguous) | 94 | 380.39 | Ultra Secure | Financial credentials |
| 19 | 75 | Full (no ambiguous) | 94 | 475.49 | Ultra Secure | Password manager keys |
| 20 | 128 | Full (no ambiguous) | 94 | 811.50  | Ultra Secure | Cryptographic keys |

**Notes**:
- Full character set (no ambiguous): 26 uppercase + 26 lowercase + 10 digits + 32 symbols = 94 characters.
- Ambiguous characters: `I`, `l`, `O`, `0`, `1`, `` ` ``.

---

### Example Passwords
Below are sample passwords for select modes:

#### Block I (Length 24, with ambiguous)
**Mode 1: Lowercase + Special**
```bash
python3 entropy_password_generator/password_generator.py --mode 1
```
```
Generated password: &]*yl>fhqs*e<.+fl=~ijy-i
Entropy: 138.75 bits
```

**Mode 8: Uppercase + Lowercase + Special**
```bash
python3 entropy_password_generator/password_generator.py --mode 8
```
```
Generated password: NmP<ToUHnm*:m\u:Rhspj=:w
Entropy: 151.16 bits
```

#### Block II (Mixed configurations)
**Mode 11: Full, no ambiguous (length 15)**
```bash
python3 entropy_password_generator/password_generator.py --mode 11
```
```
Generated password: ?*WjM\MR-.JkQr5
Entropy: 95.10 bits
```

**Mode 20: Full, no ambiguous (length 128)**
```bash
python3 entropy_password_generator/password_generator.py --mode 20
```
```
Generated password: _N$q6xm,jE2Yt=7P{GAg?XS6~-RMn=]T}~?Qt_;k)5eW[k?UZH^6$Su*a7ARaNyj)X>^*FVtMw7;t\yNK.^_@DZpQ\\K,B}qKRZ}3&}Tp&QP^H>M]<4Fb(*Wn7%U42t%
Entropy: 832.87 bits
```

#### Block III (Custom Configuration)
**Wi-Fi Password (15 chars, with ambiguous)**
```bash
python3 entropy_password_generator/password_generator.py --length 15
```
```
Generated password: t3FoI^XNvyuZ{Ui
Entropy: 98.57 bits
```

**Cryptographic Key (128 chars, with ambiguous)**
```bash
python3 entropy_password_generator/password_generator.py --length 128 --with-ambiguous
```
```
Generated password: [:I^+1GPk`>6YIAE\[z%mvN25I,Q{n<NnU~Yzg.g+Vlwu?n{aSNJ[JX;:%t\tFPQSMuAMok?RAPoTNwMYzy9Z)olx_5Ef+`!(!z)[b&Vr%{>9[k#Mhtdhffol4?F1b,,
Entropy: 833.00 bits
```

---

## Why High Entropy Matters
- **< 50 bits**: Vulnerable, crackable in seconds.
- **50–75 bits**: Moderately secure, risky for high-value targets.
- **75–100 bits**: Strong, suitable for personal and professional use.
- **> 100 bits**: Very strong, ideal for sensitive applications.

High entropy mitigates:
- Brute-force attacks (online/offline).
- Credential stuffing.
- Rainbow table attacks (with salting).

---

## Practical Applications in Mobile Devices
The table below compares mobile authentication methods to EntroPy's passwords:

| Method | Entropy | Combinations | Security | Crack Time | Use Case |
|--------|---------|--------------|----------|------------|----------|
| Pattern 3x3 | 9–18 bits | 389,000 | Very low | Seconds | Casual use |
| 4-Digit PIN | 13.3 bits | 10,000 | Very weak | < 1s | Not recommended |
| 6-Digit PIN | 19.9 bits | 1,000,000 | Weak | 1–2 min | Temporary use |
| 8-Character Alphanumeric | 59.5 bits | 8.4 × 10¹⁷ | Very good | Days | Professionals |
| EntroPy Mode 11 (15 chars) | 97.62 bits | ~10²⁹ | Extremely high | Years | Sensitive data |

---

## References
- [Proton© Blog](https://proton.me/blog/what-is-password-entropy)
- [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NIST SP 800-132](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Have I Been Pwned](https://haveibeenpwned.com/Passwords)

---

## Final Note
The EntroPy Password Generator uses Python's `secrets` module for cryptographic randomization, ensuring passwords exceed Proton© and NIST standards. Store passwords in a secure password manager like [Bitwarden©](https://bitwarden.com/) and use 2FA for optimal security.

---

#### Copyright © 2025 Gerivan Costa dos Santos

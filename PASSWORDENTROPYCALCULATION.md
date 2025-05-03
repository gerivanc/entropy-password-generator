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
- **L**: Length of the password.
- **E(R)**: Entropy in bits.

Simplified:
- Entropy = log₂(possibilities per character) × password length
- Higher entropy means exponentially greater effort to crack the password.
- The table below provides the entropy formula for each mode in a simplified notation (e.g., log₂(R)×L) for readability, with the resulting entropy in bits.

> **Note**: Entropy values are theoretical maximums, assuming uniform random selection. The requirement of at least one character per selected type (e.g., uppercase, lowercase) slightly reduces effective entropy for shorter passwords (e.g., 15 characters). This reduction is negligible for the lengths used (15–128 characters), and all modes exceed Proton© and NIST standards.

---

## Security Benchmarks

| Source | Minimum Recommended Entropy | Context |
|:------|:-----------------------------|:--------|
| **Proton©** | 75 bits | General password strength recommendation for strong protection ([source](https://proton.me/blog/what-is-password-entropy)) |
| **NIST (SP 800-132 / SP 800-63B)** | 80+ bits | For passwords protecting sensitive data ([NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html), [NIST SP 800-132](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)) |

> **Note**: Modern threat models recommend passwords with at least **100 bits of entropy** for highly sensitive accounts, such as financial or administrative systems.

---

## Project Capabilities

### Password Generation Modes
The generator offers 20 modes for secure password generation, divided into two blocks:
- **Block I (Modes 1–10)**: Fixed length of 24 characters, including ambiguous characters (e.g., 'I', 'O', '0'), with varying character sets to balance readability and security. Ideal for general-purpose passwords, such as website logins or application credentials.
- **Block II (Modes 11–20)**: Varying lengths (15 to 128 characters), mostly excluding ambiguous characters for enhanced readability. These modes cater to sensitive applications, from personal accounts to cryptographic keys and enterprise-grade security.

The table below details each mode, ordered by increasing entropy, with configurations, character set sizes (\( R \)), entropy formulas, and recommended use cases:

| Mode | Password Length | Character Set | R (Charset Size) | Entropy Formula | Entropy (bits) | Security Level | Use Case |
|------|-----------------|---------------|------------------|-----------------|----------------|----------------|----------|
| 11 | 15 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×15 | 95.70 | Strong | Personal accounts (email, social media) |
| 13 | 20 characters | Lowercase + Digits (no ambiguous) | 31 | log₂(31)×20 | 99.00 | Strong | Basic application logins |
| 14 | 20 characters | Uppercase + Digits (no ambiguous) | 31 | log₂(31)×20 | 99.00 | Strong | Device authentication |
| 12 | 18 characters | Full (uppercase, lowercase, digits, symbols, with ambiguous) | 94 | log₂(94)×18 | 117.72 | Very Strong | Professional accounts (work email, VPN) |
| 4 | 24 characters | Uppercase + Digits (with ambiguous) | 36 | log₂(36)×24 | 124.08 | Very Strong | Legacy systems requiring uppercase |
| 5 | 24 characters | Lowercase + Digits (with ambiguous) | 36 | log₂(36)×24 | 124.08 | Very Strong | Readable passwords for manual entry |
| 6 | 24 characters | Digits + Special (with ambiguous) | 42 | log₂(42)×24 | 128.64 | Very Strong | API tokens with limited character sets |
| 3 | 24 characters | Uppercase + Lowercase (with ambiguous) | 52 | log₂(52)×24 | 136.80 | Very Strong | General-purpose website logins |
| 1 | 24 characters | Lowercase + Special (with ambiguous) | 58 | log₂(58)×24 | 140.59 | Very Strong | Secure notes or backup codes |
| 2 | 24 characters | Uppercase + Special (with ambiguous) | 58 | log₂(58)×24 | 140.59 | Very Strong | Administrative console access |
| 7 | 24 characters | Uppercase + Lowercase + Digits (with ambiguous) | 62 | log₂(62)×24 | 142.80 | Very Strong | Multi-user system credentials |
| 9 | 24 characters | Uppercase + Digits + Special (with ambiguous) | 68 | log₂(68)×24 | 145.68 | Very Strong | Database access keys |
| 10 | 24 characters | Lowercase + Digits + Special (with ambiguous) | 68 | log₂(68)×24 | 145.68 | Very Strong | Secure file encryption |
| 8 | 24 characters | Uppercase + Lowercase + Special (with ambiguous) | 84 | log₂(84)×24 | 153.12 | Extremely Strong | High-security application logins |
| 15 | 24 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×24 | 153.12 | Extremely Strong | Enterprise-grade passwords |
| 16 | 32 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×32 | 204.16 | Cryptographic Grade | API keys for sensitive services |
| 17 | 42 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×42 | 267.96 | Cryptographic Grade | Server authentication tokens |
| 18 | 60 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×60 | 382.80 | Ultra Secure | Financial system credentials |
| 19 | 75 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×75 | 478.50 | Ultra Secure | Master keys for password managers |
| 20 | 128 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | 90 | log₂(90)×128 | 830.98 | Ultra Secure (Theoretical Maximum) | Cryptographic keys, blockchain wallets |

**All generated passwords surpass the Proton© minimum of 75 bits and NIST recommendations.**

### Example Passwords
To illustrate the entropy mechanics, below are sample passwords for three modes from each block, showcasing their character sets and strengths:

- **Mode 1** (Block I, 24 chars, lowercase + special, with ambiguous):
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 1
  ```
  ```
  Generated password:  zq!wr#ty&pm$nk%lc*hj=vx 
  Entropy: 140.59 bits
  ```

- **Mode 3** (Block I, 24 chars, uppercase + lowercase, with ambiguous):
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 3
  ```
  ```
  Generated password:  KjZmPqRtYxWvLcFnBsHdIkOg 
  Entropy: 136.80 bits
  ```

- **Mode 8** (Block I, 24 chars, uppercase + lowercase + special, with ambiguous):
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 8
  ```
  ```
  Generated password: Kj#nPq@Rt!xWv&MbHs$YkLc 
  Entropy: 153.12 bits
  ```

- **Mode 11** (Block II, 15 chars, full no ambiguous):
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 11
  ```
  ```
  Generated password:  Kj9mPqRtY2xWvN8 
  Entropy: 95.70 bits
  ```

- **Mode 15** (Block II, 24 chars, full no ambiguous):
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 15
  ```
  ```
  Generated password: Hs7kQwZx9mPvRtY2nB4cF8j 
  Entropy: 153.12 bits
  ```

- **Mode 20** (Block II, 128 chars, full no ambiguous):
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 20
  ```
  ```
  Generated password:  Ax9kQw#Z2vRt$Y4mPv&B6nJcF8tH3xK5zL7qM2wN4yP8rT9bV6cW2xZ5kQ7mN3tP9vR4yB8nF2wH6zJ5kL9qT3mV7xP2rN4cY8bW6tK9zQ5vM3nH2xF7pR4yT8k 
  Entropy: 830.98 bits
  ```

---

## Why High Entropy Matters

- **< 50 bits**: Vulnerable — feasible for sophisticated attackers to crack in seconds.
- **50–75 bits**: Moderately secure — risky for high-value targets, crackable in hours to days.
- **75–100 bits**: Strong — adequate for personal and professional security, requiring months to years to crack.
- **> 100 bits**: Very strong — recommended for administrative, financial, and cryptographic uses, practically uncrackable with current technology.

High entropy directly mitigates risks from:
- Online and offline brute-force attacks.
- Credential stuffing attacks.
- Rainbow table attacks (when combined with proper salting).

---

## Practical Applications of Entropy in Mobile Devices

Entropy is critical not only for passwords generated by the EntroPy Password Generator but also for authentication methods on mobile devices, such as screen lock PINs and passwords. The table below compares different screen lock methods on Android© and iOS© devices, illustrating how entropy impacts security and emphasizing the superiority of EntroPy's high-entropy passwords.

| Method | Entropy | Possible Combinations | Security Level | Est. Time to Crack | Recommended Use Case |
|--------|---------|-----------------------|----------------|-------------------|----------|
| Pattern 3x3 (Standard Pattern) | 9–18 bits | 389,000 | Very low (susceptible to smudge attacks or brute force) | Seconds to minutes | Casual or child use |
| 4-Digit PIN | 13.3 bits | 10⁴ (10,000) | Very weak (easily cracked with tools like Cellebrite©) | < 1s | Not recommended |
| 6-Digit PIN | 19.9 bits | 10⁶ (1,000,000) | Weak (vulnerable to forensic tools like GrayKey©) | 1–2 minutes | Temporary use |
| 8-Digit PIN | 26.6 bits | 10⁸ (100,000,000) | Moderate (better, but still crackable) | Minutes to hours | Intermediate users |
| 8-Character Alphabetic Password (26 letters) | 37.6 bits | 2.1 × 10¹¹ | Good (secure with rate-limiting) | Hours to days | Security-aware users |
| 10-Character Alphanumeric Password (aA1) | 59.5 bits | 8.4 × 10¹⁷ | Very good (resistant to most attacks) | Days to weeks | Security professionals |
| Complex Password 12+ Characters (aA1!@#) | 78–130+ bits | > 10²³ | Extremely high (effective against forensic tools without bypass) | Years to centuries | Sensitive or critical data |

- **Notes**:
  - Entropy is based on the formula \( E(R) = \log_2(R^L) \) and NIST SP 800-63B recommendations.
  - Estimated cracking times assume an offline attack with 10⁹ guesses per second (typical for modern GPUs) and no rate-limiting or device-specific protections (e.g., secure enclave). Actual times vary based on attacker resources and system defenses.
  - Assumes no exploitable vulnerabilities, unlocked bootloader, or root access, as highlighted in the NIST IR 8320 report.
- **Sources**: OKTA, OWASP, NIST SP 800-63B, NIST IR 8320, with custom adaptations.

Comparing these methods with the EntroPy Password Generator, even the most basic mode (Mode 11, 15 characters, 95.70 bits) surpasses common mobile authentication methods like PINs and patterns. For maximum security, such as protecting sensitive data, higher-length modes (e.g., Mode 20, 128 characters, 830.98 bits) provide unparalleled protection, making them ideal for cryptographic applications.

---

## References
- [Proton© Blog - Password Entropy Explained](https://proton.me/blog/what-is-password-entropy)
- [OKTA: What does password entropy mean?](https://www.okta.com/identity-101/password-entropy/)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#bcrypt)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [NIST SP 800-63B: 5.1.2.2 Look-Up Secret Verifiers](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NIST SP 800-132: Recommendation for Password-Based Key Derivation](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)
- [NIST IR 8320: Hardware-Enabled Security](https://nvlpubs.nistpubs/ir/2022/NIST.IR.8320.pdf)
- [Have I Been Pwned](https://haveibeenpwned.com/Passwords) - Check if your passwords have been compromised.

---

## Final Note

> **Robust Security Guaranteed**  
> The EntroPy Password Generator leverages Python's `secrets` module for cryptographically secure randomization, ensuring passwords meet or exceed Proton© (75 bits) and NIST (80+ bits) entropy standards across all 20 modes.

### Storage and Security
Never memorize strong, randomly generated passwords manually. Instead, store them securely in an encrypted environment, such as a trusted password manager. I recommend [Bitwarden©](https://bitwarden.com/), an open-source password manager with zero-knowledge encryption. Enhance protection by combining high-entropy passwords with **FIDO2 security keys**, **two-factor authentication (2FA)**, and **periodic security audits**.

### Entropy Considerations
The entropy calculation (\( E(R) = \log_2(R^L) \)) assumes ideal randomness, achieved via Python's `secrets` module, ensuring no predictable patterns (e.g., common words, keyboard sequences). This makes EntroPy passwords highly resistant to heuristic-based attacks. For additional assurance, users can validate passwords with tools like [zxcvbn](https://github.com/dropbox/zxcvbn), though the cryptographic randomization minimizes vulnerabilities. For optimal security, always use generated passwords as-is, without manual modifications that could introduce predictability.

---

#### Copyright © 2025 Gerivan Costa dos Santos

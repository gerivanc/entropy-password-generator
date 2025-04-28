# Password Entropy Calculation
![Badge: Entropy Compliant](https://img.shields.io/badge/Entropy%20Compliant-Proton%C2%A9%20%26%20NIST-brightgreen)

## Overview

The EntroPy Password Generator creates passwords with high entropy to maximize resistance against brute-force attacks. Entropy measures password strength, indicating the computational effort required to guess a password. All 20 generation modes produce passwords exceeding the Proton© (75 bits) and NIST (80+ bits) recommendations, ensuring robust security.

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

## Security Benchmarks

| Source | Minimum Recommended Entropy | Context |
|:------|:-----------------------------|:--------|
| **Proton©** | 75 bits | General password strength recommendation for strong protection ([source](https://proton.me/blog/what-is-password-entropy)) |
| **NIST (SP 800-132 / SP 800-63B)** | 80+ bits | For passwords protecting sensitive data ([NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html), [NIST SP 800-132](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)) |

> **Note**: Modern threat models recommend passwords with at least **100 bits of entropy** for highly sensitive accounts.

## Project Capabilities

The generator offers 20 modes for secure password generation, each with distinct entropy levels. The table below lists all modes, ordered by increasing entropy, with their configurations, entropy formulas, and security levels:

| Mode | Password Length | Character Set | Entropy Formula | Entropy (bits) | Security Level |
|------|-----------------|---------------|-----------------|----------------|----------------|
| 11 | 15 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×15 | 95.70 | Strong |
| 13 | 20 characters | Lowercase + Digits (no ambiguous) | log₂(31)×20 | 99.00 | Strong |
| 14 | 20 characters | Uppercase + Digits (no ambiguous) | log₂(31)×20 | 99.00 | Strong |
| 12 | 18 characters | Full (uppercase, lowercase, digits, symbols, with ambiguous) | log₂(94)×18 | 117.72 | Very Strong |
| 4 | 24 characters | Uppercase + Digits (with ambiguous) | log₂(36)×24 | 124.08 | Very Strong |
| 5 | 24 characters | Lowercase + Digits (with ambiguous) | log₂(36)×24 | 124.08 | Very Strong |
| 6 | 24 characters | Digits + Special (with ambiguous) | log₂(42)×24 | 128.64 | Very Strong |
| 3 | 24 characters | Uppercase + Lowercase (with ambiguous) | log₂(52)×24 | 136.80 | Very Strong |
| 1 | 24 characters | Lowercase + Special (with ambiguous) | log₂(58)×24 | 139.92 | Very Strong |
| 2 | 24 characters | Uppercase + Special (with ambiguous) | log₂(58)×24 | 139.92 | Very Strong |
| 7 | 24 characters | Uppercase + Lowercase + Digits (with ambiguous) | log₂(62)×24 | 142.80 | Very Strong |
| 9 | 24 characters | Uppercase + Digits + Special (with ambiguous) | log₂(68)×24 | 145.68 | Very Strong |
| 10 | 24 characters | Lowercase + Digits + Special (with ambiguous) | log₂(68)×24 | 145.68 | Very Strong |
| 8 | 24 characters | Uppercase + Lowercase + Special (with ambiguous) | log₂(84)×24 | 153.12 | Extremely Strong |
| 15 | 24 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×24 | 153.12 | Extremely Strong |
| 16 | 32 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×32 | 204.16 | Cryptographic Grade |
| 17 | 42 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×42 | 267.96 | Cryptographic Grade |
| 18 | 60 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×60 | 382.80 | Ultra Secure |
| 19 | 75 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×75 | 478.50 | Ultra Secure |
| 20 | 128 characters | Full (uppercase, lowercase, digits, symbols, no ambiguous) | log₂(90)×128 | 816.64 | Ultra Secure (Theoretical Maximum) |

**All generated passwords surpass the Proton© minimum of 75 bits and NIST recommendations.**

## Why High Entropy Matters

- **< 50 bits**: Vulnerable — feasible for sophisticated attackers to crack.
- **50–75 bits**: Moderately secure — risky for high-value targets.
- **75–100 bits**: Strong — adequate for personal and professional security.
- **> 100 bits**: Very strong — recommended for administrative, financial, and cryptographic uses.

High entropy directly mitigates risks from:
- Online and offline brute-force attacks.
- Credential stuffing attacks.
- Rainbow table attacks (when combined with proper salting).

## References

- [Proton© Blog - Password Entropy Explained](https://proton.me/blog/what-is-password-entropy)
- [NIST SP 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NIST SP 800-132 Recommendation for Password-Based Key Derivation](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)

## Final Note

> **Robust Security Guaranteed**  
> The EntroPy Password Generator leverages Python's `secrets` module for cryptographically secure randomization, ensuring passwords meet or exceed Proton© (75 bits) and NIST (80+ bits) entropy standards across all 20 modes.

### Storage and Security
Never memorize strong, randomly generated passwords manually. Instead, store them securely in an encrypted environment, such as a trusted password manager. I recommend [Bitwarden©](https://bitwarden.com/), an open-source password manager with zero-knowledge encryption. Enhance protection by combining high-entropy passwords with **FIDO2 security keys**, **two-factor authentication (2FA)**, and **periodic security audits**.

### Entropy Considerations
The entropy calculation (\( E(R) = \log_2(R^L) \)) assumes ideal randomness, where each character is independently selected from the character set. This provides a theoretical maximum strength, which the generator achieves using the `secrets` module. However, in real-world scenarios, attackers may use heuristic-based tools (e.g., [zxcvbn](https://github.com/dropbox/zxcvbn)) to detect predictable patterns, such as common words or keyboard sequences, potentially reducing effective entropy. While the generator minimizes such patterns through cryptographic randomization, users can further validate password strength with tools like zxcvbn for a complementary, practical assessment. For optimal security, always use generated passwords as-is, without manual modifications that could introduce predictability.

#### Copyright © 2025 Gerivan Costa dos Santos

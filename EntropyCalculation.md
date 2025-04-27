# Password Entropy Calculation
![Badge: Entropy Compliant](https://img.shields.io/badge/Entropy%20Compliant-Proton%C2%A9%20%26%20NIST-brightgreen)

## Overview

This project generates passwords based on cryptographic best practices, prioritizing high entropy to ensure maximum resistance against brute-force attacks.  
Entropy is a critical metric for password strength, directly correlating with the difficulty an attacker faces when attempting to guess a password.

## How Entropy is Calculated

The generator uses the standard entropy formula:

\[ E(R) = \log_2(R^L) \]

where:

- **R** = Number of possible characters (character set size)
- **L** = Length of the password
- **E(R)** = Entropy in bits

Simplified:

- Entropy=log2​(possibilities per character)×password length;
- A higher entropy value means exponentially more effort required to crack the password via brute-force methods.

## Security Benchmarks

| Source | Minimum Recommended Entropy | Context |
|:------|:-----------------------------|:--------|
| **Proton©** | 75 bits | General password strength recommendation for strong protection ([source](https://proton.me/blog/what-is-password-entropy)) |
| **NIST (SP 800-132 / SP 800-63B)** | 80+ bits | For passwords protecting sensitive data ([**NIST SP 800-63B**](https://pages.nist.gov/800-63-3/sp800-63b.html) and [**NIST SP 800-132**](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)) |

> **Note**: Modern threat models recommend passwords with at least **100 bits of entropy** for highly sensitive accounts.

---

## Project Capabilities

This password generator offers **20 modes**, ensuring generated passwords achieve the following entropy levels:

| Password Length | Character Set | Entropy (bits) | Security Level |
|:----------------|:--------------|:---------------|:---------------|
| 15 characters | Full (uppercase, lowercase, digits, symbols) | 95.10 bits | Strong |
| 18 characters | Full (uppercase, lowercase, digits, symbols) | 117.14 bits | Very Strong |
| 24 characters | Full (uppercase, lowercase, digits, symbols) | 152.16 bits | Extremely Strong |
| 32 characters | Full (uppercase, lowercase, digits, symbols) | 202.88 bits | Cryptographic Grade |
| 42 characters | Full (uppercase, lowercase, digits, symbols) | 266.27 bits | Ultra Secure |
| 60 characters | Full (uppercase, lowercase, digits, symbols) | 380.39 bits | Ultra Secure |
| 75 characters | Full (uppercase, lowercase, digits, symbols) | 475.49 bits | Ultra Secure |
| 128 characters | Full (uppercase, lowercase, digits, symbols) | 811.50 bits | Ultra Secure (Theoretical Maximum) |

**All generated passwords surpass the Proton© minimum of 75 bits and NIST recommendations.**

---

## Why High Entropy Matters

- **< 50 bits**: Vulnerable — feasible for sophisticated attackers to crack.
- **50–75 bits**: Moderately secure — risky for high-value targets.
- **75–100 bits**: Strong — adequate for personal and professional security.
- **> 100 bits**: Very strong — recommended for administrative, financial, and cryptographic uses.

High entropy **directly mitigates** the risks associated with:

- Online and offline brute-force attacks
- Credential stuffing attacks
- Rainbow table attacks (when combined with proper salting)

---

## References

- [Proton© Blog - Password Entropy Explained](https://proton.me/blog/what-is-password-entropy)
- [NIST SP 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NIST SP 800-132 Recommendation for Password-Based Key Derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-132.pdf)

---

## Final Note

To maximize protection, it is critical **never to memorize** strong, randomly generated passwords manually. Instead, these passwords must be securely stored in an encrypted environment, such as a trusted password manager.  
I use and highly recommend **[Bitwarden©](https://bitwarden.com/)**, an open-source password manager that implements zero-knowledge encryption and adheres to strong security standards. 

Additionally, combine the use of high-entropy passwords with advanced security layers such as **FIDO2 security keys**, **two-factor authentication (2FA)**, and **periodic security audits** to maintain a resilient defense posture.

---

#### Copyright © 2025 Gerivan Costa dos Santos

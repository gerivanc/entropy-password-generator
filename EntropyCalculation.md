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

\[ Entropy = \log_2(\text{possibilities per character}) \times \text{password length} \]

A higher entropy value means exponentially more effort required to crack the password via brute-force methods.

## Security Benchmarks

| Source | Minimum Recommended Entropy | Context |
|:------|:-----------------------------|:--------|
| **Proton\u00a9** | 75 bits | General password strength recommendation for strong protection ([source](https://proton.me/blog/what-is-password-entropy)) |
| **NIST (SP 800-132 / SP 800-63B)** | 80+ bits | For passwords protecting sensitive data ([source](https://pages.nist.gov/800-63-3/sp800-63b.html)) |

> **Note**: Modern threat models recommend passwords with at least **100 bits of entropy** for highly sensitive accounts.

---

## Project Capabilities

This password generator offers **20 modes**, ensuring generated passwords achieve the following entropy levels:

| Password Length | Character Set | Entropy (bits) | Security Level |
|:----------------|:--------------|:---------------|:---------------|
| 15 characters | Full (uppercase, lowercase, digits, symbols) | 95.10 bits | Strong |
| 20 characters | Full | 126.80 bits | Very Strong |
| 25 characters | Full | 158.50 bits | Extremely Strong |
| 32 characters | Full | 203.84 bits | Cryptographic Grade |
| 64 characters | Full | 407.68 bits | Ultra Secure |
| 128 characters | Full | 811.50 bits | Ultra Secure (Theoretical Maximum) |

**All generated passwords surpass the Proton\u00a9 minimum of 75 bits and NIST recommendations.**

---

## Why High Entropy Matters

- **< 50 bits**: Vulnerable \u2014 feasible for sophisticated attackers to crack.
- **50\u201375 bits**: Moderately secure \u2014 risky for high-value targets.
- **75\u2013100 bits**: Strong \u2014 adequate for personal and professional security.
- **> 100 bits**: Very strong \u2014 recommended for administrative, financial, and cryptographic uses.

High entropy **directly mitigates** the risks associated with:

- Online and offline brute-force attacks
- Credential stuffing attacks
- Rainbow table attacks (when combined with proper salting)

---

## References

- [Proton\u00a9 Blog \u2013 Password Entropy Explained](https://proton.me/blog/what-is-password-entropy)
- [NIST SP 800-63B \u2013 Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [NIST SP 800-132 \u2013 Recommendation for Password-Based Key Derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-132.pdf)

---

## Final Note

To maximize protection, it is critical **never to memorize** strong, randomly generated passwords manually. Instead, these passwords must be securely stored in an encrypted environment, such as a trusted password manager.  
I use and highly recommend **[Bitwarden©](https://bitwarden.com/)**, an open-source password manager that implements zero-knowledge encryption and adheres to strong security standards. 

Additionally, combine the use of high-entropy passwords with advanced security layers such as **FIDO2 security keys**, **two-factor authentication (2FA)**, and **periodic security audits** to maintain a resilient defense posture.

---

#### Copyright © 2025 Gerivan Costa dos Santos



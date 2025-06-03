# Security Policy

## ✅ Supported Versions

The following versions of the EntroPy Password Generator are currently supported with security updates. Unsupported versions will not receive patches for vulnerabilities. To check your installed version, run `entropy-password-generator --version`.

| Version | Supported          | End-of-Life Date       |
|---------|--------------------|------------------------|
| 0.6.x   | :white_check_mark: | TBD (Est. June 2026)    |
| 0.5.x   | :white_check_mark: | January 31, 2026      |
| < 0.5   | :x:                | -                      |

## 🧪 Test PyPI Usage

The Test PyPI release of EntroPy Password Generator is intended for testing and development purposes only. It may contain experimental features or unpatched vulnerabilities and should not be used in production environments. For production use, install the stable version from the official Python Package Index (PyPI) at [https://pypi.org/project/entropy-password-generator/](https://pypi.org/project/entropy-password-generator/).

## 🛡️ Security Best Practices

To ensure the secure use of EntroPy Password Generator:
- Use Python 3.8 or higher, keeping it updated to the latest patch version.
- Install the tool in a virtual environment to isolate dependencies.
- Verify package integrity during installation by checking the package's hash or signature (available on the [PyPI project page](https://pypi.org/project/entropy-password-generator/)).
- Store generated passwords securely using a trusted password manager, such as [Bitwarden](https://bitwarden.com/).

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in the EntroPy Password Generator, please report it promptly to protect the community. We consider vulnerabilities such as cryptographic weaknesses, insecure random number generation, or code execution flaws within scope. Follow these steps:

1. **Where to Report**: Email [dean-grumbly-plop@duck.com](mailto:dean-grumbly-plop@duck.com) with a detailed description of the vulnerability, including steps to reproduce, impact, and affected versions. For sensitive reports, request our PGP key for encrypted communication.
2. **Expected Response Time**: You will receive an acknowledgment within 48 hours. A detailed update, including assessment and resolution plan, will be provided within 7 business days.
3. **Resolution Process**:
   - **Accepted Vulnerabilities**: We will prioritize a fix based on severity (e.g., critical issues patched within 30 days) and deploy it in the next supported release. We may coordinate with CVE authorities for public disclosure.
   - **Declined Vulnerabilities**: If the issue is not reproducible, out of scope, or not a vulnerability, you will be notified with an explanation.
4. **Responsible Disclosure Timeline**:
   - Acknowledgment: Within 48 hours.
   - Initial assessment: Within 7 business days.
   - Patch release: Within 30–60 days, depending on severity.
   - Public disclosure: Coordinated with the reporter, typically after the patch is released.
5. **Confidentiality**: Do not disclose the vulnerability publicly until we have resolved it and provided clearance. Responsible reporters may be acknowledged publicly (with consent) in release notes or a project "Hall of Fame."
6. **Contact for Queries**: For questions about the process, email [dean-grumbly-plop@duck.com](mailto:dean-grumbly-plop@duck.com).

## 📚 Additional Resources

- [README.md](https://github.com/gerivanc/entropy-password-generator/blob/main/README.md) for project overview and installation.
- [RELEASE.md](https://github.com/gerivanc/entropy-password-generator/blob/main/RELEASE.md) for version-specific details.
- [CONTRIBUTING.md](https://github.com/gerivanc/entropy-password-generator/blob/main/CONTRIBUTING.md) for contribution guidelines.
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) for general security guidance.
- [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) for password strength standards.

We appreciate your cooperation in responsibly reporting vulnerabilities to maintain the security of the EntroPy Password Generator.

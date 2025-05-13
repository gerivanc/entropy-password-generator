# EntroPy Password Generator v0.5.3

**Release Date**: May 13, 2025

## 📋 Overview
The **EntroPy Password Generator** v0.5.3 is now available on [Test PyPI](https://test.pypi.org/project/entropy-password-generator/) and [PyPI](https://pypi.org/project/entropy-password-generator/)! This release builds on the improvements from v0.5.3, adding a GitHub Actions badge to the project documentation to reflect the status of CI/CD workflows and updating the version references to v0.5.3. It continues to provide 20+ secure password generation modes, with entropies from 97.62 to 833.00 bits, exceeding Proton© and NIST standards.

## ✨ What's New
- **GitHub Actions Badge**: Added a badge to `README.md` to display the status of GitHub Actions workflows (e.g., `python-app.yml`), enhancing visibility into the project's CI/CD pipeline health.
- **Version Update**: Updated version references in `README.md` from `0.5.0` to `0.5.3`, ensuring consistency across documentation and package metadata.
- **Retained Improvements from v0.5.1**:
  - Enhanced CLI output with blank lines before and after the `Password` field for better readability across all modes and custom configurations.
  - Updated "Screenshots" section in `README.md` with new images hosted on Google Drive, showcasing the improved password output layout for Mode 15 and a custom configuration with `--length 85`.

## 🔧 Installation
### Installation from PyPI (Stable Version)
To install the latest stable version of the EntroPy Password Generator (version 0.5.2) from PyPI, run the following command:

```bash
pip install entropy-password-generator==0.5.3
```

This command will install the package globally or in your active Python environment. After installation, you can run the generator using:

```bash
entropy-password-generator
```

Visit the [PyPI project page](https://pypi.org/project/entropy-password-generator/) for additional details about the stable release.

### Installation from Test PyPI (Development Version)
To test the latest development version of the EntroPy Password Generator, install it from the Test Python Package Index (Test PyPI):

```bash
pip install -i https://test.pypi.org/simple/ entropy-password-generator
```

## ▶️ Usage
Generate a password with mode 1:

```bash
entropy-password-generator --mode 1
```

## 📬 Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **EntroPy Password Generator**! 🚀🔑

---

#### Copyright © 2025 Gerivan Costa dos Santos

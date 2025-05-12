# EntroPy Password Generator v0.5.1

**Release Date**: May 11, 2025

## Overview
The **EntroPy Password Generator** v0.5.1 is now available on [Test PyPI](https://test.pypi.org/project/entropy-password-generator/) and [PyPI](https://pypi.org/project/entropy-password-generator/)! This release enhances the CLI output formatting for better readability, updates project documentation, and prepares for the stable PyPI release (v0.5.1). It includes 20 secure password generation modes, with entropies from 97.62 to 833.00 bits, exceeding Proton© and NIST standards.

## What's New
- **Enhanced CLI Output**: Added blank lines before and after the `Password` field in the CLI output, improving visual separation between `Custom Password` (or `Mode X Password`), `Password`, and `Length` fields for all modes (1-20 via `--mode`) and custom configurations (15-128 characters via `--length`).
- **Updated Documentation**: Refreshed the "Screenshots" section in `README.md` with new images hosted on Google Drive, showcasing the updated password output layout for Mode 15 (`python3 entropy_password_generator/password_generator.py --mode 15`) and a custom configuration with `--length 85` (`python3 entropy_password_generator/password_generator.py --length 85`).

## Installation
### Installation from PyPI (Stable Version)
To install the latest stable version of the EntroPy Password Generator (version 0.5.1) from PyPI, run the following command:

```bash
pip install entropy-password-generator==0.5.1
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

## Usage
Generate a password with mode 1:

```bash
entropy-password-generator --mode 1
```

See the [CHANGELOG.md](https://github.com/gerivanc/entropy-password-generator/blob/main/CHANGELOG.md) for a complete list of changes.

## Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **EntroPy Password Generator**! 🚀🔑

---

#### Copyright © 2025 Gerivan Costa dos Santos

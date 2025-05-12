# EntroPy Password Generator v0.5.1

**Release Date**: May 11, 2025

## Overview
The **EntroPy Password Generator** v0.5.1 is now available on [Test PyPI](https://test.pypi.org/project/entropy-password-generator/) and [PyPI](https://pypi.org/project/entropy-password-generator/)! This release enhances the CLI experience, improves project documentation, and prepares for the upcoming PyPI release (v0.5.1). It includes 20 secure password generation modes, with entropies from 97.62 to 833.00 bits, exceeding Proton© and NIST standards.

## What's New
- **Improved CLI**: Added support for `--mode` to select specific password generation modes (1-20).
- **Issue Template**: Standardized issue reporting with a new template in [Issue Template](https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).
- **Documentation**: Updated `README.md` with a "Reporting Issues" section and enhanced usage examples.
- **Security**: Added `SECURITY.md` for vulnerability reporting.

## Installation
### Installation from PyPI (Stable Version)
To install the latest stable version of the EntroPy Password Generator (version 0.4.9) from PyPI, run the following command:

```bash
pip install entropy-password-generator==0.5.0
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

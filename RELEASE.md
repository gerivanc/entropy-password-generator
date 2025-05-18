# EntroPy Password Generator v0.5.6

**Release Date**: May 18, 2025

---

## 📋 Overview
The **EntroPy Password Generator** v0.5.6 is now available on [Test PyPI](https://test.pypi.org/project/entropy-password-generator/) and [PyPI](https://pypi.org/project/entropy-password-generator/)! This release builds on the improvements from v0.5.6, adding a GitHub Actions badge to the project documentation to reflect the status of CI/CD workflows and updating the version references to v0.5.6. It continues to provide 20+ secure password generation modes, with entropies from 97.62 to 833.00 bits, exceeding Proton© and NIST standards.

---

## ✨ What's New
- **GitHub Actions Badge**: Added a badge to `README.md` to display the status of GitHub Actions workflows (e.g., `python-app.yml`), enhancing visibility into the project's CI/CD pipeline health.
- **Version Update**: Updated version references in `README.md` from `0.5.0` to `0.5.6`, ensuring consistency across documentation and package metadata.
- **Retained Improvements from v0.5.6**:
  - Enhanced CLI output with blank lines before and after the `Password` field for better readability across all modes and custom configurations.
  - Updated "Screenshots" section in `README.md` with new images hosted on Google Drive, showcasing the improved password output layout for Mode 15 and a custom configuration with `--length 85`.

---

## 🔧Installation
Ensure you have Python 3.8 or higher installed. You can install the package directly from PyPI or TestPyPI, or clone the repository to test locally.

### Cloning the Repository
To work with the source code or test the package locally, clone the repository and set up a virtual environment:

```bash
git clone https://github.com/gerivanc/entropy-password-generator.git
cd entropy-password-generator
```

---

## 🔧Installation from PyPI (Stable Version)
To install the latest stable version of the EntroPy Password Generator (version 0.5.6) from PyPI, run the following command:

```bash
source testenv/bin/activate
pip install entropy-password-generator
```

This command will install the package globally or in your active Python environment. After installation, you can run the generator using:

```bash
entropy-password-generator --mode 11
```

or

```bash
entropy-password-generator --length 15
```

Visit the [PyPI project page](https://pypi.org/project/entropy-password-generator/) for additional details about the stable release.

---

## 🔧Installation from Test PyPI (Development Version)
To test the latest development version of the EntroPy Password Generator, install it from the Test Python Package Index (Test PyPI):

```bash
python3 -m venv venv-testpypi
source venv-testpypi/bin/activate
pip install -i https://test.pypi.org/simple/ entropy-password-generator
```

This command will install the package globally or in your active Python environment. After installation, you can run the generator using:

```bash
entropy-password-generator --mode 20
```

or

```bash
entropy-password-generator --length 128 --with-ambiguous
```

Visit the [Test PyPI project page](https://test.pypi.org/project/entropy-password-generator/) for additional details about the stable release.

---

##📬 Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **EntroPy Password Generator**! 🚀🔑

---

#### Copyright © 2025 Gerivan Costa dos Santos

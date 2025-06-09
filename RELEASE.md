# EntroPy Password Generator v0.6.1

**Release Date:** June 09th, 2025

Released on 	2025/05/02 	

Last updated 	2025/06/09 

Publisher 	[gerivanc](https://github.com/gerivanc/)

Changelog [Changelog](https://github.com/gerivanc/entropy-password-generator/blob/main/CHANGELOG.md)

Release Notes [RELEASE.md](https://github.com/gerivanc/entropy-password-generator/blob/main/RELEASE.md)

Reporting Issues	[Report a](https://github.com/gerivanc/entropy-password-generator/issues/new/choose)

---

## 📋 Overview
The **EntroPy Password Generator** v0.6.1 is now available on [Test PyPI](https://test.pypi.org/project/entropy-password-generator/) and [PyPI](https://pypi.org/project/entropy-password-generator/)! This release builds on the improvements from v0.6.1, adding a GitHub Actions badge to the project documentation to reflect the status of CI/CD workflows and updating the version references to v0.6.1. It continues to provide 20+ secure password generation modes, with entropies from 97.62 to 833.00 bits, exceeding Proton© and NIST standards.

---

## ✨ What's New
Updated version references in `README.md` from `0.6.0` to `0.6.1`. Updates to all layout structures and section titles. 

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

### 🔧Installation from PyPI (Stable Version)
To install the latest stable version of the EntroPy Password Generator (version 0.6.1) from PyPI, run the following command:

```bash
python3 -m venv venv-stablepypi
source venv-stablepypi/bin/activate
pip install entropy-password-generator
pip install --upgrade pip
pip list
```

This command will install the package globally or in your active Python environment. After installation, you can run the generator using:

```bash
entropy-password-generator --mode 11
```

or

```bash
entropy-password-generator --length 15
```

When finished, deactivate the virtual environment.:
   ```bash
   deactivate
   ```

Visit the [PyPI project page](https://pypi.org/project/entropy-password-generator/) for additional details about the stable release.

---

### 🔧Installation from Test PyPI (Development Version)
To test the latest development (version 0.6.1) of the EntroPy Password Generator, install it from the Test Python Package Index (Test PyPI):

```bash
python3 -m venv venv-testpypi
source venv-testpypi/bin/activate
pip install -i https://test.pypi.org/simple/ --trusted-host test.pypi.org entropy-password-generator
pip install --upgrade pip
pip list
```

This command will install the package globally or in your active Python environment. After installation, you can run the generator using:

```bash
entropy-password-generator --mode 20
```

or

```bash
entropy-password-generator --length 128 --with-ambiguous
```

When finished, deactivate the virtual environment.:
   ```bash
   deactivate
   ```

Visit the [Test PyPI project page](https://test.pypi.org/project/entropy-password-generator/) for additional details about the development version.

---

## 🖥️ Getting Started on Windows
For Windows users, a dedicated guide is available to help you install and use the **EntroPy Password Generator** via **PowerShell**. This step-by-step tutorial covers installation, configuration, and password generation with clear examples tailored for the Windows environment, including detailed instructions for setting up Git and running the generator. Check out the [**GETTING_STARTED_WINDOWS.md**](https://github.com/gerivanc/entropy-password-generator/blob/main/GETTING_STARTED_WINDOWS.md) for comprehensive guidance.

---

## 📬Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **EntroPy Password Generator**! 🚀🔑

---

#### Copyright © 2025 Gerivan Costa dos Santos

# Release to EntroPy Password Generator v0.6.4

🔸 **Release Date:** August 07th, 2025

🔸 Released on 	2025/05/02 	

🔸 Last updated 	2025/08/07 

- Publisher [gerivanc](https://github.com/gerivanc/)

- Changelog [Changelog](https://github.com/gerivanc/entropy-password-generator/blob/main/CHANGELOG.md)

- Release Notes [RELEASE.md](https://github.com/gerivanc/entropy-password-generator/blob/main/RELEASE.md)

- Reporting Issues	[Report a](https://github.com/gerivanc/entropy-password-generator/issues/new/choose)

---

# 📋 Overview
The **EntroPy Password Generator** v0.6.4 is now available on [Test PyPI](https://test.pypi.org/project/entropy-password-generator/) and [PyPI](https://pypi.org/project/entropy-password-generator/)! This release builds on the improvements from v0.6.4, adding a GitHub Actions badge to the project documentation to reflect the status of CI/CD workflows and updating the version references to v0.6.4. It continues to provide 20+ secure password generation modes, with entropies from 97.62 to 833.00 bits, exceeding Proton© and NIST standards.

---

# ✨ What's New
- Updated version references in `README.md` from `0.6.3` to `0.6.4`. Updates to all layout structures and section titles. 
- Adjusted layout styling and emoji use for better readability and visual identity.
- Corrected anchor links in the Table of Contents that were not functioning due to emoji or formatting conflicts. 

---

# 📦 Install in simulated environment

### 🛠️ Installation Options for use in virtual environments on Test PyPI and PyPI (Stable Version) on Kali Linux. 

## 📝 Overview
The `entropy-password-generator` package can be installed from PyPI (Stable Version) or Test PyPI (Development Version) using a virtual environment. The automated installation scripts have been tested and confirmed to work successfully on **Parrot OS**. On **Kali Linux**, due to system-specific configurations, the automated scripts may encounter issues. For successful installation on Kali Linux, use the simplified manual installation steps provided below.

## 📦 Stable Version Installation (PyPI)

To install the stable version from PyPI on Kali Linux, execute the following commands step-by-step:

```bash
python3 -m venv venv-stablepypi
source venv-stablepypi/bin/activate
python -m ensurepip --upgrade
pip install --upgrade pip
pip install entropy-password-generator
pip list
```

## 🧪 Development Version Installation (Test PyPI)

To install the development version from Test PyPI on Kali Linux, execute the following commands step-by-step:

```bash
python3 -m venv venv-testpypi
source venv-testpypi/bin/activate
python -m ensurepip --upgrade
pip install --upgrade pip
pip install -i https://test.pypi.org/simple/ --trusted-host test.pypi.org entropy-password-generator
pip list
```

---

### 📋 Notes
- These manual steps ensure the creation of a virtual environment, activation, and installation of the package from either PyPI or Test PyPI without errors.
- For exclusive software deals and tools for developers, check out [Dealsbe - Exclusive Software Deals for Developers and Startups](https://dealsbe.com).
- For further assistance or troubleshooting, please refer to the project documentation or contact the support team.

---

###  🛠️ Installation Options for use in virtual environments on Test PyPI and PyPI (Stable Version) on Parrot OS. 

## 📝 Overview
To avoid conflicts with the system, install it in a virtual environment, such as Kali Linux and/or Parrot. 
The **EntroPy Password Generator** can be installed from the Python Package Index (PyPI) for the stable release or from the Test Python Package Index (Test PyPI) to test the latest development version. Follow the instructions below based on your needs.

## 🔧 Installation from PyPI (Stable Version)
To install the latest stable version of the EntroPy Password Generator (version 0.6.4) from PyPI, run the following command:

```bash
#!/bin/bash

# Exit immediately if any command fails
set -e

echo "🔧 Creating virtual environment: venv-stablepypi..."
python3 -m venv venv-stablepypi

echo "✅ Virtual environment created successfully."

echo "⚙️ Activating virtual environment..."
source venv-stablepypi/bin/activate

echo "🔄 Ensuring pip is available in the environment..."
python -m ensurepip --upgrade

echo "⬆️ Upgrading pip to the latest version..."
pip install --upgrade pip

echo "📦 Installing the entropy-password-generator package from PyPI..."
pip install entropy-password-generator

echo "📋 Listing installed packages:"
pip list

echo "🚀 Installation completed successfully!"
```

This command installs the package globally or in your active Python environment. After installation, you can run the generator using the following commands:

Generate a custom length password of 15 ambiguous characters: 
```bash
entropy-password-generator --length 15 --with-ambiguous
```

or

Generate a password with default mode 20: 
```bash
entropy-password-generator --mode 20
```

When finished, deactivate the virtual environment.:
   ```bash
   deactivate
   ```

Visit the [PyPI project page](https://pypi.org/project/entropy-password-generator/) for additional details about the stable release.

## 🔧 Installation from Test PyPI (Development Version)
To test the latest development version of the EntroPy Password Generator, install it from the Test Python Package Index (Test PyPI):

```bash
#!/bin/bash

# Exit immediately if any command fails
set -e

echo "🔧 Creating virtual environment: venv-testpypi..."
python3 -m venv venv-testpypi

echo "✅ Virtual environment created successfully."

echo "⚙️ Activating virtual environment..."
source venv-testpypi/bin/activate

echo "🔄 Ensuring pip is available in the environment..."
python -m ensurepip --upgrade

echo "⬆️ Upgrading pip to the latest version..."
pip install --upgrade pip

echo "📦 Installing the entropy-password-generator package from Test PyPI..."
pip install -i https://test.pypi.org/simple/ --trusted-host test.pypi.org entropy-password-generator

echo "📋 Listing installed packages:"
pip list

echo "🚀 Installation completed successfully!"
```

This command installs the package globally or in your active Python environment. After installation, you can run the generator using the following commands:

Generate a custom length password of 42 ambiguous characters: 
```bash
entropy-password-generator --length 42 --with-ambiguous
```

or

Generate a password with default mode 11: 
```bash
entropy-password-generator --mode 11
```

When finished, deactivate the virtual environment.:
   ```bash
   deactivate
   ```

Visit the [Test PyPI project page](https://test.pypi.org/project/entropy-password-generator/) for additional details about the development version.

> **Note:** the execution of the `--mode` and `--length` scripts, as demonstrated in the previous options such as: `entropy-password-generator --mode 11` and `entropy-password-generator --length 42 --with-ambiguous`, are specific for use in the active virtual environment. Do not use > > them after cloning the repository via CLI directly without the active virtual environment, if you use them you will receive an error message such as: `entropy-password-generator: command not found`.
> 
> To use the `--mode` and `--length` scripts used via CLI directly after cloning the repository without activating the virtual environment,
> use the scripts such as: `python3 entropy_password_generator/password_generator.py --mode 11` (mode 1 to 20) and custom mode `python3 entropy_password_generator/password_generator.py --length 42 --with-ambiguous` (using custom 15 to 128 characters).  

---

## 🖥️ Getting Started on Windows
For Windows users, a dedicated guide is available to help you install and use the **EntroPy Password Generator** via **PowerShell**. This step-by-step tutorial covers installation, configuration, and password generation with clear examples tailored for the Windows environment, including detailed instructions for setting up Git and running the generator. Check out the [**GETTING_STARTED_WINDOWS.md**](https://github.com/gerivanc/entropy-password-generator/blob/main/GETTING_STARTED_WINDOWS.md) for comprehensive guidance.

---

## 📬Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/entropy-password-generator/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **EntroPy Password Generator**! 🚀🔑

---

#### Copyright © 2025 Gerivan Costa dos Santos

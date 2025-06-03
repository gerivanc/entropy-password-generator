# Getting Started with EntroPy Password Generator on Windows PowerShell

Welcome to the **EntroPy Password Generator**, a secure and customizable tool for generating robust passwords! This guide provides step-by-step instructions for installing and using the **EntroPy Password Generator** via the Windows PowerShell command-line interface (CLI). Whether you're securing personal accounts or generating cryptographic keys, this guide will help you get started quickly and efficiently.

---

## 📋 Prerequisites

Before diving in, ensure your Windows environment is ready:

- **Operating System**: Windows 10 or later (PowerShell 5.1 or higher is included by default).
- **Python**: Version 3.8 or higher installed. Download it from [python.org](https://www.python.org/downloads/) if needed.
- **pip**: Python's package manager, typically included with Python. Verify by running:
  ```powershell
  pip --version
  ```
  If not installed, follow the [official pip installation guide](https://pip.pypa.io/en/stable/installation/).
- **PowerShell**: Use Windows PowerShell (pre-installed) or PowerShell Core (download from [Microsoft](https://learn.microsoft.com/en-us/powershell/)).
- **Internet Connection**: Required for downloading the package from PyPI or cloning the repository.

---

## 🛠️ Installation Options

There are two primary ways to install **EntroPy Password Generator** on Windows: via **PyPI** for the stable version or by **cloning the repository** from GitHub. Below, we detail both methods using PowerShell.

### Option 1: Install from PyPI (Stable Version)

This is the easiest method to get started with the latest stable release. Visit the [PyPI project page](https://pypi.org/project/entropy-password-generator/) for additional details on the latest development release.

1. **Open PowerShell**:
   - Press `Win + S`, type `PowerShell`, and select **Windows PowerShell**.
   - Alternatively, press `Win + R`, type `powershell`, and hit Enter.

2. **Create a Virtual Environment (Recommended)**:
   Virtual environments prevent conflicts with system-wide Python packages.
   ```powershell
   python -m venv entropy_venv
   .\entropy_venv\Scripts\Activate.ps1
   ```
   After activation, you’ll see `(entropy_venv)` in your PowerShell prompt.

3. **Install EntroPy Password Generator**:
   ```powershell
   pip install entropy-password-generator
   ```
   This installs the package globally or within the active virtual environment.

4. **Verify Installation**:
   ```powershell
   entropy-password-generator --help
   ```
   If successful, you’ll see the CLI help menu with available options.

### Option 2: Install from GitHub Repository

This method is ideal for users who want to explore the source code or contribute to the project. Since many users may be unfamiliar with Git, we’ll provide detailed steps to install and use it.

1. **Install Git**:
   - **Download Git**: Visit [git-scm.com](https://git-scm.com/download/win) and download the latest version of Git for Windows.
   - **Run the Installer**:
     - Follow the installation wizard, accepting the default settings unless you have specific preferences.
     - Ensure the option “Add Git to PATH” is selected (usually enabled by default) to make Git accessible in PowerShell.
   - **Verify Git Installation**:
     Open PowerShell and run:
     ```powershell
     git --version
     ```
     If installed correctly, you’ll see output like `git version 2.x.x`. If you get an error (e.g., `git : The term 'git' is not recognized`), ensure Git was added to your system PATH. You can fix this by reinstalling Git and selecting the “Add Git to PATH” option, or manually adding the Git executable path (e.g., `C:\Program Files\Git\bin`) to your system’s environment variables:
     - Press `Win + R`, type `sysdm.cpl`, and go to **Advanced > Environment Variables**.
     - Under **System Variables**, find `Path`, edit it, and add the Git bin directory (e.g., `C:\Program Files\Git\bin`).

2. **Clone the Repository**:
   In PowerShell, navigate to a directory where you want to store the project (e.g., `C:\Projects`):
   ```powershell
   cd C:\Projects
   git clone https://github.com/gerivanc/entropy-password-generator.git
   cd entropy-password-generator
   ```

3. **Run Without Installation**:
   No additional dependencies are required since the project uses only Python standard libraries. You can run the generator directly:
   ```powershell
   python entropy_password_generator\password_generator.py --help
   ```

---

## 🔑 Generating Passwords

Once installed, you can generate passwords using the CLI. Below are examples of common use cases, leveraging the predefined modes or custom configurations.

### Using Predefined Modes

The **EntroPy Password Generator** offers 20+ predefined modes for secure password generation. Here’s how to use them in PowerShell:

- **Generate a Password with Mode 15 (24 characters, high entropy)**:
  ```powershell
  entropy-password-generator --mode 15
  ```
  **Example Output**:
  ```
  Generated password: 9gj-%Jb,zw8s3Gxsg(k#%.Q7
  Entropy: 152.16 bits
  ```

- **Generate a Password with Mode 20 (128 characters, ultra-secure)**:
  ```powershell
  entropy-password-generator --mode 20
  ```
  **Example Output**:
  ```
  Generated password: Zt(^Xw&,\%(j~3szY$nmPkyWq<Xv=q*~9AajA25.#cvs$FVgU:?>e?d$Un2A!E@.rAwEA]ef$4&fK5B{zm7?pe#GE;#;pv\A[,JSZF~2xYN\k((2!#mVN6rQK.G$%cjT
  Entropy: 811.50 bits
  ```

> **Note**: If you cloned the repository and are not using the PyPI installation, replace `entropy-password-generator` with:
> ```powershell
> python entropy_password_generator\password_generator.py --mode <number>
> ```

### Using Custom Configurations

For tailored passwords, use the `--length` option with additional flags to customize the character set.

- **Generate a 15-Character Wi-Fi Password (with ambiguous characters)**:
  ```powershell
  entropy-password-generator --length 15 --with-ambiguous
  ```
  **Example Output**:
  ```
  Generated password: D(LcKs|exNf_zf3
  Entropy: 97.62 bits
  ```

- **Generate a 32-Character Cloud Storage Password (no ambiguous characters)**:
  ```powershell
  entropy-password-generator --length 32
  ```
  **Example Output**:
  ```
  Generated password: z;#JTR^S<pY<D7jvB268<!4~NPrSe~$N
  Entropy: 202.88 bits
  ```

- **Generate a Simple Readable Password (15 characters, lowercase + digits, no ambiguous)**:
  ```powershell
  entropy-password-generator --length 15 --no-uppercase --no-special
  ```
  **Example Output**:
  ```
  Generated password: 76bgqz8b9keftaf
  Entropy: 74.31 bits
  ```
  > **Warning:** Password entropy ({entropy:.2f} bits) is below the recommended 75 bits (Proton© standard).
  > To improve security, increase the password length (e.g., use `--length 24` or higher) and include more character types (e.g., use uppercase, lowercase, digits, and special characters).
.

- **Generate a 128-Character Cryptographic Key (with ambiguous characters)**:
  ```powershell
  entropy-password-generator --length 128 --with-ambiguous
  ```
  **Example Output**:
  ```
  Generated password: CwjKwYd1#^1W)_odEjmKFrY=K+9c5$Q0UaKH5MH;I4fFj:YJMlXkQkhkiL]T+M.1*[O&s~Lfw\^UPBVf=(t7Bi3QWZL~lO-7p\g;=Dq91|SP3!@Onj$E3d]!MZ,7Tz)^
  Entropy: 833.00 bits
  ```

---

## 🖥️ PowerShell Tips for Smooth Usage

- **Check Python Version**:
  ```powershell
  python --version
  ```
  Ensure it’s 3.8 or higher.

- **Update pip**:
  To avoid compatibility issues:
  ```powershell
  python -m pip install --upgrade pip
  ```

- **Run Commands from Repository**:
  If you cloned the repository, navigate to the project folder and use:
  ```powershell
  python entropy_password_generator\password_generator.py --mode <number>
  ```

- **View CLI Help**:
  For a full list of options:
  ```powershell
  entropy-password-generator --help
  ```

---

## ⚠️ Troubleshooting

- **Command Not Found**:
  - Ensure you’ve installed the package globally or are using the correct command for the repository (`python entropy_password_generator\password_generator.py`).
  - If using the repository, verify you’re in the correct directory.

- **pip Install Fails**:
  - Update pip: `python -m pip install --upgrade pip`.
  - Ensure an active internet connection.
  - Check for permission issues; try running PowerShell as Administrator:
    ```powershell
    Start-Process powershell -Verb RunAs
    ```

- **Git Not Recognized**:
  - If `git --version` fails, ensure Git is installed and added to your system PATH. Reinstall Git, selecting “Add Git to PATH,” or manually add the Git bin directory (e.g., `C:\Program Files\Git\bin`) to your environment variables.

- **Python Not Recognized**:
  - Verify Python is installed and added to your system PATH. Reinstall Python and check the “Add Python to PATH” option during installation.

- **Low Entropy Warning**:
  - If a password’s entropy is below 75 bits, increase the length (e.g., `--length 24`) or include more character types (e.g., remove `--no-uppercase` or `--no-special`).

For additional help, visit the [Issues tab](https://github.com/gerivanc/entropy-password-generator/issues) on GitHub.

---

## 🔒 Security Best Practices

- **Use a Password Manager**: Store generated passwords in a secure password manager like [Bitwarden](https://bitwarden.com/).
- **Enable 2FA**: Add two-factor authentication for critical accounts.
- **Avoid Reusing Passwords**: Generate unique passwords for each service.
- **Regular Updates**: Update your master passwords periodically using high-entropy modes (e.g., Mode 19 or 20).

---

## 🌟 Next Steps

Explore the full range of password modes and configurations in the [README.md](https://github.com/gerivanc/entropy-password-generator/blob/main/README.md). For detailed entropy calculations, check [PASSWORDENTROPYCALCULATION.md](https://github.com/gerivanc/entropy-password-generator/blob/main/PASSWORDENTROPYCALCULATION.md).

Want to contribute? See our [Contributing Guidelines](https://github.com/gerivanc/entropy-password-generator/blob/main/CONTRIBUTING.md) to join the project!

---

## 📬 Contact

For questions or feedback, reach out at: [dean-grumbly-plop@duck.com](mailto:dean-grumbly-plop@duck.com).

---

#### Copyright © 2025 Gerivan Costa dos Santos

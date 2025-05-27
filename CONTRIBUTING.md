# Contributing to EntroPy Password Generator

Thank you for your interest in contributing to the **EntroPy Password Generator**! This project provides a secure and customizable password generation tool, compliant with Proton© and NIST standards, and we welcome contributions to enhance its functionality, documentation, and accessibility. Whether you're fixing bugs, adding features, improving documentation, or contributing in other ways, your efforts are greatly appreciated.

---

## 🤝 Ways to Contribute

You can contribute to the EntroPy Password Generator in several ways:
- **Code**: Fix bugs, add new features, or optimize existing functionality in `password_generator.py`.
- **Documentation**: Improve `README.md`, `SECURITY.md`, `RELEASE.md`, or add inline comments and docstrings.
- **Issues**: Report bugs, suggest features, or propose documentation enhancements via GitHub Issues.
- **Translations**: Translate documentation or CLI messages to other languages.
- **Media**: Create or update screenshots, logos, or other visual assets for the project.
- **Testing**: Validate functionality across different Python versions or platforms.

---

## 🚀 Getting Started

### ⚙️ 1. Setting Up Your Environment
To contribute, set up a local development environment:
1. **Install Python**: Ensure you have Python 3.8 or higher installed, as specified in `pyproject.toml`.
2. **Clone the repository**:
   ```bash
   git clone https://github.com/gerivanc/entropy-password-generator.git
   cd entropy-password-generator
   ```
3. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   **On Windows**:
   ```bash
   python -m venv entropy_venv
   .\entropy_venv\Scripts\Activate.ps1
   ```
4. **Install development tools** (optional, but recommended):
   ```bash
   pip install flake8 black isort
   ```
   These tools help ensure code quality:
   - `flake8`: Linting to enforce PEP 8.
   - `black`: Automatic code formatting.
   - `isort`: Sorting imports.

### 📢 2. Reporting Issues
If you find a bug, have a feature request, or notice documentation that needs improvement:
- **Search existing issues**: Check the [GitHub Issues page](https://github.com/gerivanc/entropy-password-generator/issues) to avoid duplicates.
- **Use templates**: Follow the issue templates in `.github/ISSUE_TEMPLATE/` for bug reports or feature requests.
- **Provide details**: Include a clear title, description, steps to reproduce (if applicable), expected behavior, and screenshots or logs.
- **Security issues**: For vulnerabilities, follow the process in [SECURITY.md](https://github.com/gerivanc/entropy-password-generator/blob/main/SECURITY.md) instead of opening a public issue.

### 🔄 3. Submitting Pull Requests
To contribute code, documentation, or other changes, submit a pull request (PR):
1. **Fork the repository**:
   - Click the "Fork" button on the [repository page](https://github.com/gerivanc/entropy-password-generator).
   - Clone your fork:
     ```bash
     git clone https://github.com/gerivanc/entropy-password-generator.git
     cd entropy-password-generator
     ```
2. **Create a branch**:
   - Use a descriptive name (e.g., `feature/add-new-mode`, `fix/bug-entropy-calc`):
     ```bash
     git checkout -b feature/your-feature-name
     ```
3. **Make changes**:
   - Follow the coding standards below.
   - Test changes locally (see "Testing" section).
   - Update documentation (e.g., `README.md`, docstrings) if necessary.
   - Run linting and formatting tools:
     ```bash
     flake8 entropy_password_generator/
     black entropy_password_generator/
     isort entropy_password_generator/
     ```
4. **Commit changes**:
   - Use clear, concise commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) format (e.g., `feat: add new password mode`, `fix: correct entropy calculation`):
     ```bash
     git commit -m "feat: describe your change"
     ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a pull request**:
   - Go to the [repository](https://github.com/gerivanc/entropy-password-generator) and click "New pull request".
   - Select your branch and provide a detailed description of your changes.
   - Reference related issues (e.g., "Fixes #123").
   - Ensure your PR passes the GitHub Actions CI checks (if configured).

### 📜 4. Coding Standards
To maintain consistency and security, adhere to these guidelines:
- **Python Version**: Use Python 3.8 or higher, as specified in `pyproject.toml`.
- **Style**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for code style. Use `flake8` for linting and `black` for formatting.
- **Docstrings**: Write clear, English docstrings in [Google style](https://google.github.io/styleguide/pyguide.html) for all functions and modules.
- **Security**: Use the `secrets` module for cryptographic randomness. Avoid insecure libraries like `random`. If introducing new dependencies, justify their necessity and security.
- **File Structure**: Keep changes within the existing structure (e.g., core logic in `entropy_password_generator/password_generator.py`).
- **Licensing**: By contributing, you agree that your contributions are licensed under the [MIT License](https://github.com/gerivanc/entropy-password-generator/blob/main/LICENSE.md).

### 🧪 5. Testing
Ensure your changes do not break existing functionality:
- **Manual Testing**:
  - Run the CLI with different modes and configurations:
    ```bash
    python3 entropy_password_generator/password_generator.py --mode 1
    python3 entropy_password_generator/password_generator.py --length 15 --no-special
    ```
  - If the package is installed (e.g., from Test PyPI):
    ```bash
    entropy-password-generator --mode 1
    ```
  - Note: Use the direct path (`python3 entropy_password_generator/password_generator.py`) or CLI command (`entropy-password-generator`) to avoid `RuntimeWarning` issues with `python -m`.
- **Cross-Version Testing**:
  - Test with Python 3.8, 3.10, and 3.12 to ensure compatibility. Use tools like `tox` or a GitHub Actions matrix if available.
- **Automated Tests**:
  - Currently, the project does not include automated tests. If adding tests, use `pytest` and place them in a `tests/` directory. Example:
    ```bash
    pip install pytest
    pytest tests/
    ```
  - Contributions that add test coverage are highly encouraged.
- **Validation**:
  - Verify that new modes or configurations align with the `MODES` dictionary in `password_generator.py`.
  - Check that entropy calculations remain accurate and compliant with Proton© (75+ bits) and NIST standards.

### ✅ 6. Pull Request Review Process
After submitting a PR:
- **Review Time**: The maintainer will review your PR within 7 business days. Complex changes may take longer.
- **Criteria**: PRs are evaluated based on code quality, adherence to standards, security, and alignment with project goals.
- **Feedback**: You may be asked to make revisions. Address feedback promptly to expedite merging.
- **Approval**: PRs require approval from the maintainer (Gerivan Costa dos Santos) before merging.
- **CI Checks**: Ensure all GitHub Actions checks (if configured) pass. Fix any failures reported in the workflow.

### 🤗 7. Code of Conduct
We are committed to fostering an inclusive and respectful community. Please:
- Be kind, respectful, and professional in all interactions.
- Avoid offensive language, harassment, or discriminatory behavior.
- Report inappropriate behavior to the maintainer at [dean-grumbly-plop@duck.com](mailto:dean-grumbly-plop@duck.com).
Violations may result in exclusion from the project.

### ❓ 8. Getting Help
For questions or assistance:
- Read the [README.md](https://github.com/gerivanc/entropy-password-generator/blob/main/README.md) for project details.
- Check the [SECURITY.md](https://github.com/gerivanc/entropy-password-generator/blob/main/SECURITY.md) for vulnerability reporting.
- Open an issue on the [GitHub Issues page](https://github.com/gerivanc/entropy-password-generator/issues).
- Contact the maintainer at [dean-grumbly-plop@duck.com](mailto:dean-grumbly-plop@duck.com).

### 🙌 9. Acknowledgments
Thank you for contributing to the **EntroPy Password Generator**! Your efforts help make this tool more secure, accessible, and valuable for users worldwide. Significant contributors may be acknowledged in the project’s documentation or release notes (with your consent).

---

#### Copyright © 2025 Gerivan Costa dos Santos

# Contributing to EntroPy Password Generator

Thank you for your interest in contributing to the **EntroPy Password Generator**! This project aims to provide a secure and customizable password generation tool, and we welcome contributions from the community to make it even better. Whether you're fixing bugs, adding features, or improving documentation, your help is greatly appreciated.

## How to Contribute

### 1. Reporting Issues
If you find a bug, have a feature request, or notice documentation that needs improvement, please open an issue on the [GitHub Issues page](https://github.com/gerivanc/entropy-password-generator/issues).
- **Search first**: Check existing issues to avoid duplicates.
- **Provide details**: Include a clear title, description, steps to reproduce (if applicable), and any relevant screenshots or logs.
- **Use templates**: If available, use the issue templates provided in the repository.

### 2. Submitting Pull Requests
We encourage contributions via pull requests (PRs). To submit a PR:
1. **Fork the repository**:
   - Click the "Fork" button at the top of the [repository page](https://github.com/gerivanc/entropy-password-generator).
   - Clone your fork:
     ```bash
     git clone https://github.com/gerivanc/entropy-password-generator.git
     cd entropy-password-generator
     ```
2. **Create a branch**:
   - Use a descriptive branch name:
     ```bash
     git checkout -b feature/your-feature-name
     ```
3. **Make changes**:
   - Follow the coding standards below.
   - Test your changes locally (e.g., `python3 entropy_password_generator/password_generator.py --mode 1` or `python3 entropy_password_generator/password_generator.py --length 20 --no-special`). Ensure compatibility with the `MODES` dictionary in `password_generator.py` for mode-based generation.
   - Update documentation if necessary (e.g., `README.md` or inline comments).
4. **Commit changes**:
   - Write clear, concise commit messages:
     ```bash
     git commit -m "Add feature: describe your change"
     ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a pull request**:
   - Go to the [repository](https://github.com/gerivanc/entropy-password-generator) and click "New pull request".
   - Select your branch and describe your changes in the PR description.
   - Reference any related issues (e.g., "Fixes #123").

### 3. Coding Standards
To maintain consistency, please adhere to the following guidelines:
- **Language**: Use Python 3.6+ and follow PEP 8 style guidelines.
- **Comments and Docstrings**: Write clear comments and docstrings in English for all functions and complex logic.
- **Security**: Ensure changes maintain the use of the `secrets` module for cryptographic randomness.
- **Testing**: Test your changes locally to ensure they don’t break existing functionality. After cloning the repository, run:
  ```bash
  python3 entropy_password_generator/password_generator.py --mode 1
  ```
  or
  ```bash
  python3 entropy_password_generator/password_generator.py --length 15
  ```
  Alternatively, if you have installed the package from Test PyPI (`pip install -i https://test.pypi.org/simple/ entropy-password-generator`), you can test using:
  ```bash
  entropy-password-generator --mode 1
  ```
  **Note**: It is recommended to use the direct path (`python3 entropy_password_generator/password_generator.py`) or the CLI command (`entropy-password-generator`) instead of `python -m` to avoid the `RuntimeWarning` that may occur due to module import behavior.
- **File Structure**: Keep changes within the existing structure (e.g., update `password_generator.py` for core changes).

### 4. Code of Conduct
We are committed to fostering an inclusive and respectful community. Please:
- Be kind and respectful in all interactions.
- Avoid offensive language or behavior.
- Report any inappropriate behavior to the project maintainer at dean-grumbly-plop@duck.com.

### 5. Getting Help
If you have questions or need assistance:
- Check the [README](https://github.com/gerivanc/entropy-password-generator/blob/main/README.md) for usage details.
- Open an issue with your question.
- Contact the maintainer at dean-grumbly-plop@duck.com.

## Acknowledgments
Thank you for contributing to the **EntroPy Password Generator**! Your efforts help make this project a valuable tool for secure password generation.

---

#### Copyright © 2025 Gerivan Costa dos Santos

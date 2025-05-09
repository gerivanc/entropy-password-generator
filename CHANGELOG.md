# Changelog

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-orange)](https://keepachangelog.com/en/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-blue)](https://semver.org/spec/v2.0.0.html)

All notable changes to the EntroPy Password Generator project are documented in this file. This project adheres to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard, which ensures a structured and human-readable format for tracking changes. By following this approach, we provide clear visibility into the project's evolution, making it easier for users and contributors to understand what has been added, changed, or fixed in each release. Additionally, the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which uses a versioning scheme of MAJOR.MINOR.PATCH. This practice enhances predictability and compatibility by clearly indicating the impact of updates: major versions for breaking changes, minor versions for new features, and patch versions for bug fixes. Together, these standards improve the project's maintainability, transparency, and usability for developers and security enthusiasts.

## [0.5.0] - 2025-05-08

### Added
- Added a new section in `README.md` titled "Installation Options," detailing installation of the stable version (0.4.9) via PyPI (`pip install entropy-password-generator==0.4.9`) and the development version via Test PyPI (`pip install -i https://test.pypi.org/simple/ entropy-password-generator`), including links to the PyPI and Test PyPI project pages.
- Added two new badges in `README.md`: one for the PyPI project (`https://pypi.org/project/entropy-password-generator/0.4.9/`) and one for Test PyPI (`https://test.pypi.org/project/entropy-password-generator/`), highlighting package availability.
- Added a note in `README.md` on avoiding the `RuntimeWarning` when running the script, recommending the direct path (`python3 entropy_password_generator/password_generator.py`) or package installation.
- Added a new section in `README.md` titled "Screenshots," including Google Drive links to images showing CLI outputs for Mode 15 (`python3 entropy_password_generator/password_generator.py --mode 15`) and a custom configuration with `--length 85` (`python3 entropy_password_generator/password_generator.py --length 85`).
- Added Block III (Custom Configuration) in `README.md` under the "Password Modes" section, introducing custom modes with lengths from 15 to 128 characters, including ambiguous characters by default, with entropies ranging from 97.62 to 833.00 bits.
- Added five custom configuration examples in `README.md` under Block III, covering scenarios such as Wi-Fi password (15 characters), cloud storage services (32 characters), simple readable password (15 characters), API token (24 characters), and cryptographic key (128 characters).
- Added a table in `README.md` titled "Suggestions for Password Types," recommending six modes (8, 9, 10, 15, 19, 20) for specific services, such as high-security website logins, password manager master keys, and cryptographic keys.
- Added a new section in `README.md` titled "Support This Project" with a PayPal donation button (`https://www.paypal.com/ncp/payment/FYUGSCLQRSQDN`), encouraging support for project development.
- Added a "Character Set Size (R)" column to the password modes summary table in `README.md`, indicating the size of the character set (e.g., 90 for full set, 36 for uppercase + digits).
- Added a "Use Case" column to the password modes summary table in `README.md`, suggesting practical applications for each mode (e.g., personal accounts, API tokens, cryptographic keys).

### Fixed
- Fixed linting errors in `password_generator.py` identified by Flake8:
  - Corrected E302 by adding two blank lines before the `generate_password()` function.
  - Resolved E501 by breaking long lines (e.g., `all_chars = uppercase_local + lowercase_local + digits_local + special_local`) into multiple lines to respect the 79-character limit.
  - Addressed E999 by fixing inconsistent indentation (tabs vs. spaces) in the `generate_password()` function.
- Fixed output formatting in the `main()` function of `password_generator.py` by replacing literal strings with f-strings, ensuring generated passwords and entropy values are displayed correctly instead of placeholders (e.g., `{password}`, `{entropy:.2f}`).
- Corrected entropy values in the password modes summary table and examples in `README.md` for consistency (e.g., Mode 1 adjusted from 139.92 to 138.75 bits; Mode 20 adjusted from 816.64 to 811.50 bits).
- Added a note to the password modes summary table in `README.md`, clarifying that entropy values are theoretical maximums and that requiring at least one character per selected type slightly reduces effective entropy, but all modes remain compliant with Proton and NIST standards.

### Changed
- Updated the project description in `README.md` to mention "20+ modes" (previously 20 modes) and an entropy range of 97.62 to 833.00 bits (previously 95.70 to 816.64 bits), reflecting the addition of custom modes with ambiguous characters.
- Updated the "Password Entropy Calculation" section in `README.md` to include entropy examples for custom modes (e.g., `--length 15 --with-ambiguous`: 97.62 bits; `--length 128 --with-ambiguous`: 833.00 bits) and remove mention of zxcvbn, simplifying the explanation.
- Reorganized the "Using Custom Configuration" section in `README.md`, moving examples to the new Block III under "Using Predefined Modes" and focusing on specific use-case scenarios.
- Updated the "Usage" section in `README.md` to include instructions for running after PyPI/Test PyPI installation (`entropy-password-generator`) and clarify repository execution options with `--mode` and `--length`.
- Updated the version in `password_generator.py` to `0.5.0`, reflecting the latest release.

## [0.4.9] - 2025-05-03

### Added
- Added a new section in `README.md` titled "Suggestions for Password Types," featuring a table with six of the strongest password modes (Modes 8, 9, 10 from Block I; Modes 15, 19, 20 from Block II) and their recommended services (e.g., high-security website logins, password manager master keys, cryptographic keys), providing practical guidance for users.

### Changed
- Updated the version number in `README.md` to `0.4.9`, reflecting the latest release.
- Removed the "Validating Password Strength" section from `README.md` to emphasize the inherent strength of each mode and allow users to choose modes based on their specific needs.
- Removed quotes from password examples in the "Using Predefined Modes" section of `README.md` for Block I and Block II, improving visual clarity and aesthetics.

## [0.4.8] - 2025-05-02

### Added
- Published the `entropy-password-generator` package to the Test Python Package Index (Test PyPI) with version 0.4.7, enabling users to install and test the package via `pip install -i https://test.pypi.org/simple/ entropy-password-generator`. The release is available at [https://test.pypi.org/project/entropy-password-generator/](https://test.pypi.org/project/entropy-password-generator/).
- Added a new section in `README.md` titled "Installation from Test PyPI" with instructions for installing the package from Test PyPI, including the command and a link to the project’s Test PyPI page, improving accessibility for early adopters.
- Added a badge in `README.md` for the Test PyPI release, linking to [https://test.pypi.org/project/entropy-password-generator/](https://test.pypi.org/project/entropy-password-generator/), to highlight the availability of the package and encourage testing.
- Added a verification step in the `pypi-publish.yml` workflow to confirm successful publication to Test PyPI by checking the package’s availability and version on the Test PyPI index, ensuring reliability of the release process.
- Added a note in `SECURITY.md` clarifying that the Test PyPI release is intended for testing purposes and should not be used in production environments, reinforcing security best practices.
- Added an issue template (`issue_template.md`) in `.github/ISSUE_TEMPLATE/` to standardize issue reporting and improve contributor experience.
- Added `config.yml` to `.github/ISSUE_TEMPLATE/` to customize the issue creation experience, disabling blank issues and adding a security vulnerability reporting link.
- Added a "Reporting Issues" section to `README.md`, linking to the issue template to encourage community feedback and bug reporting.
- Published the `entropy-password-generator` package version 0.4.8 to the Test Python Package Index, available at [https://test.pypi.org/project/entropy-password-generator/0.4.8/](https://test.pypi.org/project/entropy-password-generator/0.4.8/).

### Changed
- Updated the "Usage" section in `README.md` to include an example of running the CLI command (`entropy-password-generator --mode 1`) after installing the package from Test PyPI, ensuring consistency with the new installation method.
- Updated the version number in `pyproject.toml` and `__init__.py` to `0.4.8` to reflect the latest changes and prepare for future releases.
- Enhanced the `pypi-publish.yml` workflow to include a step for generating a release changelog summary for version 0.4.8, extracted from `CHANGELOG.md`, to improve release documentation and visibility.
- Updated the project’s Test PyPI history link in `README.md` to point to [https://test.pypi.org/project/entropy-password-generator/#history](https://test.pypi.org/project/entropy-password-generator/#history), ensuring users can view the release history directly.
- Updated the "Coding Standards" section in `CONTRIBUTING.md` to include a note about using the `entropy-password-generator` command for testing after installation from Test PyPI, aligning with the new installation method and improving contributor guidance.
- Updated the `python-app.yml` workflow to include a step for additional validation (details incomplete in the original document).

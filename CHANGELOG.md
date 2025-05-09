# Changelog

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-orange)](https://keepachangelog.com/en/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-blue)](https://semver.org/spec/v2.0.0.html)

All notable changes to the EntroPy Password Generator project are documented in this file. This project adheres to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard, which ensures a structured and human-readable format for tracking changes. By following this approach, we provide clear visibility into the project's evolution, making it easier for users and contributors to understand what has been added, changed, or fixed in each release. Additionally, the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which uses a versioning scheme of MAJOR.MINOR.PATCH. This practice enhances predictability and compatibility by clearly indicating the impact of updates: major versions for breaking changes, minor versions for new features, and patch versions for bug fixes. Together, these standards improve the project's maintainability, transparency, and usability for developers and security enthusiasts.

## [0.5.0] - 2025-05-08

### Fixed
- Fixed linting errors in `password_generator.py` identified by Flake8:
  - Corrected E302 by adding two blank lines before the `generate_password()` function.
  - Resolved E501 by breaking long lines (e.g., `all_chars = uppercase_local + lowercase_local + digits_local + special_local`) into multiple lines to respect the 79-character limit.
  - Addressed E999 by fixing inconsistent indentation (tabs vs. spaces) in the `generate_password()` function.
- Fixed the output formatting in the `main()` function of `password_generator.py` by replacing literal strings with f-strings, ensuring that generated passwords and entropy values are displayed correctly instead of placeholders (e.g., `{password}`, `{entropy:.2f}`).

### Changed
- Updated the version number in `password_generator.py` to `0.5.0`, reflecting the latest release.

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
- Updated the `python-app.yml` workflow to include a

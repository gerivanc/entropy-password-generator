# Changelog

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-orange)](https://keepachangelog.com/en/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-blue)](https://semver.org/spec/v2.0.0.html)

All notable changes to the EntroPy Password Generator project are documented in this file. This project adheres to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard, which ensures a structured and human-readable format for tracking changes. By following this approach, we provide clear visibility into the project's evolution, making it easier for users and contributors to understand what has been added, changed, or fixed in each release. Additionally, the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which uses a versioning scheme of MAJOR.MINOR.PATCH. This practice enhances predictability and compatibility by clearly indicating the impact of updates: major versions for breaking changes, minor versions for new features, and patch versions for bug fixes. Together, these standards improve the project's maintainability, transparency, and usability for developers and security enthusiasts.

## [0.6.0] - 2025-06-03

### Changed
- Updated project version from 0.5.9 to 0.6.0 in the README.md title.
- Updates to all layout structures and section titles.
- Changes to the version indication in all files that require versioning changes.

### Fixed
- Corrected the emojis used in the main section titles of the README.md file to ensure consistent and meaningful representation, enhancing visual clarity and alignment with section content.

## [0.5.9] - 2025-05-30

### Changed
- Updated project version from 0.5.8 to 0.5.9 in the README.md title.
- Revised the **Installation** section to include updated example commands for PyPI and Test PyPI installations:
  - PyPI examples changed to demonstrate `--length 15 --with-ambiguous` and `--mode 20`.
  - Test PyPI examples changed to demonstrate `--length 42 --with-ambiguous` and `--mode 11`.
- Reorganized the **Usage** section for improved clarity, explicitly highlighting the `--with-ambiguous` option for custom configurations.
- Updated **Block III (Custom Configuration)** examples:
  - Wi-Fi Password example now explicitly includes `--with-ambiguous` for consistency.
  - Updated generated password examples for Wi-Fi Password and Cloud Storage Services, maintaining consistent entropy values.
- Updated **Screenshots** section to showcase:
  - CLI output for `--mode 11` instead of `--mode 15`.
  - CLI output for `--length 15 --with-ambiguous` instead of `--length 85 --with-ambiguous`.

### Fixed
- No functional bugs were fixed in this release, as changes were limited to documentation improvements.

### Added
- No new features were added in this release.

### Deprecated
- No features were deprecated in this release.

### Removed
- No features or content were removed in this release.

### Security
- No security vulnerabilities were addressed in this release.

## [0.5.8] - 2025-05-27
### Added
- Added detailed installation instructions in README.md for both stable and development versions of the **EntroPy Password Generator**:
  - **PyPI (Stable Version)**: Instructions for installing version 0.5.8 from PyPI in a virtual environment, including commands to create and activate a virtual environment, install the package, and run the generator with examples (`entropy-password-generator --mode 11` and `entropy-password-generator --length 15`).
  - **Test PyPI (Development Version)**: Instructions for installing the latest development version from Test PyPI in a virtual environment, including commands to create and activate a virtual environment, install the package with a trusted host, and run the generator with examples (`entropy-password-generator --mode 20` and `entropy-password-generator --length 128 --with-ambiguous`).
  - Included links to the [PyPI project page](https://pypi.org/project/entropy-password-generator/) and [Test PyPI project page](https://test.pypi.org/project/entropy-password-generator/) for additional details.
  - Provided guidance on deactivating virtual environments using the `deactivate` command.
- Recommended using virtual environments (e.g., on Kali Linux or Parrot) to avoid system conflicts during installation.

### Updated
- Enhanced README.md with a new section, "Installation Options for use in virtual environments on Test PyPI and PyPI (Stable Version)," to provide clear, step-by-step guidance for users installing the package in virtual environments.

## [0.5.7] - 2025-05-27
### Added
- Created `GETTING_STARTED_WINDOWS.md`, a comprehensive guide tailored for Windows users. This file provides step-by-step instructions for cloning the **EntroPy Password Generator** repository and generating passwords using the Windows PowerShell command-line interface (CLI). The guide emphasizes accessibility for novice users, including detailed steps for installing Git and running the generator without a virtual environment, enhancing usability for Windows-based environments.

### Updated
- Added a clarification note in README.md regarding the use of script modes in the virtual environment. The execution of the `--mode` and `--length` scripts is specific to an active virtual environment and does not apply when cloning the repository via CLI directly. Users attempting to run these scripts without activating the virtual environment will encounter an error (`entropy-password-generator: command not found`). For direct CLI usage post-cloning, alternative commands using `python3 entropy_password_generator/password_generator.py` should be followed, ensuring proper execution without dependency on a virtual environment.

### Fixed
- Clarified in README.md that the `--mode` and `--length` scripts (e.g., `entropy-password-generator --mode 20` and `entropy-password-generator --length 15`) are specific to an active virtual environment. Added instructions for direct CLI usage after cloning the repository without a virtual environment, using commands like `python3 entropy_password_generator/password_generator.py --mode 15` (modes 1 to 20) and `python3 entropy_password_generator/password_generator.py --length 70` (custom length 15 to 128 characters), to prevent errors such as `entropy-password-generator: command not found`.

## [0.5.5] - 2025-05-17

### Fixed
- Resolved `ModuleNotFoundError: No module named 'entropy_password_generator'` by adding explicit package inclusion in `pyproject.toml` (`[tool.hatch.build.targets.wheel]`), ensuring the `entropy_password_generator` module is included in the wheel for TestPyPI and PyPI installations.

### Changed
- Updated version references from `0.5.3` to `0.5.5` in `pyproject.toml`, `__init__.py`, and documentation files.
- Enhanced `RELEASE.md` with detailed installation instructions for cloning the repository, setting up virtual environments, and testing with PyPI (Stable Version) and TestPyPI (Development Version).

## [0.5.3] - 2025-05-13

## [0.5.2] - 2025-05-12

## [0.5.1] - 2025-05-11

### Changed
- Updated the `main()` function in `password_generator.py` to add blank lines (`print()`) before and after the `Password` field in the output, creating visual spacing between `Custom Password` (or `Mode X Password`), `Password`, and `Length` fields for all modes (1 to 20 via `--mode`) and custom configurations (15 to 128 characters via `--length`), enhancing readability and highlighting the generated password.
- Updated the "Screenshots" section in `README.md` to include new images hosted on Google Drive, reflecting the updated password output layout with added spacing for Mode 15 (`python3 entropy_password_generator/password_generator.py --mode 15`) and a custom configuration with `--length 85` (`python3 entropy_password_generator/password_generator.py --length 85`).

## [0.5.0] - 2025-05-10

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
- Added `bug_report.md` in `.github/ISSUE_TEMPLATE/` to provide a standardized template for bug reports, improving the contributor experience by ensuring detailed and structured issue submissions.

### Fixed
- Fixed linting errors in `password_generator.py` identified by Flake8:
  - Corrected E302 by adding two blank lines before the `generate_password()` function.
  - Resolved E501 by breaking long lines (e.g., `all_chars = uppercase_local + lowercase_local + digits_local + special_local`) into multiple lines to respect the 79-character limit.
  - Addressed E999 by fixing inconsistent indentation (tabs vs. spaces) in the `generate_password()` function.
- Fixed output formatting in the `main()` function of `password_generator.py` by replacing literal strings with f-strings, ensuring generated passwords and entropy values are displayed correctly instead of placeholders (e.g., `{password}`, `{entropy:.2f}`).
- Corrected entropy values in the password modes summary table and examples in `README.md` for consistency (e.g., Mode 1 adjusted from 139.92 to 138.75 bits; Mode 20 adjusted from 816.64 to 811.50 bits).
- Added a note to the password modes summary table in `README.md`, clarifying that entropy values are theoretical maximums and that requiring at least one character per selected type slightly reduces effective entropy, but all modes remain compliant with Proton and NIST standards.
- Fixed E501 linting error in `entropy_password_generator/__init__.py` by removing invisible whitespace before the docstring, confirmed via `hexdump`, and ensuring lines respect the 79-character limit.
- Fixed E999 IndentationError in `entropy_password_generator/__init__.py` by correcting unexpected indent (3 spaces) on the `__all__` declaration, using manual editing and `black` reformatting.
- Fixed ModuleNotFoundError during local imports by ensuring proper package installation with `pip install .`, enabling successful imports of `entropy_password_generator`.

### Changed
- Updated the project description in `README.md` to mention "20+ modes" (previously 20 modes) and an entropy range of 97.62 to 833.00 bits (previously 95.70 to 816.64 bits), reflecting the addition of custom modes with ambiguous characters.
- Updated the "Password Entropy Calculation" section in `README.md` to include entropy examples for custom modes (e.g., `--length 15 --with-ambiguous`: 97.62 bits; `--length 128 --with-ambiguous`: 833.00 bits) and remove mention of zxcvbn, simplifying the explanation.
- Reorganized the "Using Custom Configuration" section in `README.md`, moving examples to the new Block III under "Using Predefined Modes" and focusing on specific use-case scenarios.
- Updated the "Usage" section in `README.md` to include instructions for running after PyPI/Test PyPI installation (`entropy-password-generator`) and clarify repository execution options with `--mode` and `--length`.
- Updated the version in `password_generator.py` to `0.5.0`, reflecting the latest release.
- Enhanced the `python-app.yml` workflow by adding a "Reformat code with black" step to automatically correct indentation issues before linting, and added a `git diff` check to ensure changes are committed.

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
- Updated the `python-app.yml` workflow to include a step for installing the package from Test PyPI and replaced `python -m` commands with `entropy-password-generator` to avoid `RuntimeWarning` and align with the new CLI functionality.

### Fixed
- Fixed a minor typo in the `README.md` "Installation from Test PyPI" section, ensuring the pip command uses the correct index URL (`https://test.pypi.org/simple/`) for clarity and accuracy.
- Fixed the filename from `gitignore.txt` to `.gitignore` to follow standard Git conventions, with no changes to the content.

## [0.4.7] - 2025-05-01

### Added
- Added a "Visitors" section to `README.md` with a visitor counter badge using the `github-profile-views-counter` service, allowing tracking of repository visits.
- Added an optional "GitHub Stats" section to `README.md` (commented out by default) using `github-readme-stats`, providing a template for displaying GitHub statistics like stars, commits, and contributions.
- Added an explicit `dependencies = []` entry in `pyproject.toml` to clarify that the project has no external dependencies, enhancing transparency for users.
- Added a CLI entry point in `pyproject.toml` under `[project.scripts]` (`entropy-password-generator = "entropy_password_generator.password_generator:main"`), allowing users to run the generator directly via the command `entropy-password-generator` after installation.
- Added a step in `pypi-publish.yml` to clean previous build artifacts (`rm -rf dist/*`) before building the package, preventing potential conflicts during publication.
- Added a caching step for pip dependencies in `pypi-publish.yml` using `actions/cache@v3`, improving the efficiency of the publication workflow.
- Added a verification step in `pypi-publish.yml` to test the package installation from Test PyPI before publishing to the official PyPI, ensuring the package is functional.
- Added `SECURITY.md` file to provide a security policy, detailing supported versions and instructions for reporting vulnerabilities, enhancing project security practices.
- Added a "Security - Reporting a Vulnerability" section in `README.md` to inform users about the security policy and link to `SECURITY.md`, improving visibility of vulnerability reporting procedures.
- Detailed specification for usage modes in **Using Custom Configuration** in `README.md` file.

### Changed
- Updated the "Visitors" section in `README.md` to use the HITS service (hits.seeyoufarm.com) for the visitor counter badge, replacing the previous visitcount.itsvg.in service, which was found to be unavailable, ensuring reliable tracking of repository visits.
- For usage modes in Using Custom Configuration in `README.md`.

## [0.4.6] - 2025-05-01

### Changed
- Expanded the "Using Custom Configuration" section in `README.md` by adding five new examples, showcasing a wider range of customization options (e.g., short passwords with only letters, long passwords with digits and special characters, and configurations with ambiguous characters), encouraging users to explore the project's flexibility.

## [0.4.5] - 2025-05-01

### Changed
- Updated `README.md` to use the direct command path (`python3 entropy_password_generator/password_generator.py`) instead of `python -m` in the "Using Predefined Modes" and "Using Custom Configuration" sections, avoiding the `RuntimeWarning` during execution.
- Updated example passwords and entropy values in `README.md` to reflect recent test results for Modes 1, 3, 10, 12, 20, and custom configurations, ensuring consistency with the script's current output.
- Added a note in the "Usage" section of `README.md` recommending the use of the direct command path to avoid the `RuntimeWarning`, improving user experience.
- Updated `CONTRIBUTING.md` to use the correct direct command path (`python3 entropy_password_generator/password_generator.py`) in the "Coding Standards" section for test examples, ensuring accuracy.
- Added a note in the "Coding Standards" section of `CONTRIBUTING.md` recommending the use of the direct command path to avoid the `RuntimeWarning`, providing clearer guidance for contributors.

## [0.4.4] - 2025-05-01

### Changed
- Updated `CONTRIBUTING.md` to include a test example using the `--mode` argument (`python3 password_generator.py --mode 1`) in the "Submitting Pull Requests" section, reflecting the new CLI functionality and ensuring contributor awareness.
- Enhanced `pypi-publish.yml` by adding a version consistency validation step, comparing the version in `pyproject.toml` and `__init__.py` before publishing to PyPI, to prevent release errors.

## [0.4.3] - 2025-04-30

### Added
- Added `--mode <number>` argument to `password_generator.py` CLI, allowing users to select a specific predefined password generation mode (1 to 20) for Block I and Block II, simplifying the generation of individual modes.
- Added a dictionary (`MODES`) in `password_generator.py` to centralize the configurations of all 20 password generation modes, improving maintainability and scalability.
- Updated `README.md` to reflect the new `--mode` argument, including revised "CLI Options" and "Usage" sections with examples for generating passwords using `--mode` for each of the 20 modes.

### Changed
- Modified the `main()` function in `password_generator.py` to prioritize `--mode` over manual configuration arguments, generating only the password for the specified mode instead of all modes.
- Updated the CLI behavior in `password_generator.py` to display mode-specific output (e.g., "Mode X Password:") when `--mode` is used, improving user experience and clarity.
- Reorganized the "Usage" section in `README.md` to separate predefined mode usage (using `--mode`) from custom configuration, enhancing readability and usability.

## [0.4.2] - 2025-04-29

### Fixed
- Fixed an `ImportError` in `password_generator.py` by removing circular imports and ensuring proper package structure in `entropy_password_generator`.
- Fixed CLI behavior to generate a single password based on the provided arguments, aligning with the usage instructions in `README.md` for Block I and Block II modes.

## [0.4.1] - 2025-04-28

### Added
- Added execution instruction in the script header of `password_generator.py`.
- Added `__init__.py` to `entropy_password_generator/` to ensure proper package structure, with version defined.
- Added a note in the `README.md` under the "Password Entropy Calculation" section, addressing the limitations of the entropy calculation (\( E(R) = \log_2(R^L) \)). The note highlights potential overestimation in real-world scenarios and suggests using tools like `zxcvbn` for practical strength validation.
- Added a styled quote block in the `README.md` to emphasize compliance with Proton© (75 bits) and NIST (80+ bits) entropy standards, enhancing visual appeal and user trust.
- Added an entropy minimum warning in `password_generator.py`. If the entropy of a generated password is below 75 bits (Proton© standard), a warning is displayed with contextual suggestions to improve security (e.g., increase length, include more character types).
- Added badges for "Keep a Changelog" and "Semantic Versioning" at the beginning of `CHANGELOG.md`, with links to their respective websites, to highlight adherence to these standards.
- Added a debug step in the CI workflow (`.github/workflows/python-app.yml`) to display the current commit and content of `password_generator.py`, aiding in diagnosing pipeline issues.
- Added a new section titled "Practical Applications of Entropy in Mobile Devices" in `PASSWORDENTROPYCALCULATION.md`, providing practical context for entropy calculations.
- Added a table in `PASSWORDENTROPYCALCULATION.md` comparing screen lock methods on Android© and iOS© devices, with entropy values ranging from 9-18 bits to 78-130+ bits.
- Added an introductory paragraph and a comparative note in the "Practical Applications of Entropy in Mobile Devices" section of `PASSWORDENTROPYCALCULATION.md`, linking entropy concepts to the project's password generation modes.
- Added the `pyproject.toml` file to the project root, enabling modern package configuration for PyPI publication and ensuring compatibility with tools like `build` and `twine`.

### Changed
- Updated version to `0.4.1` in `password_generator.py` to reflect recent changes.
- Improved error handling in `password_generator.py` CLI with more descriptive messages and usage suggestion.
- Updated CI workflow (`python-app.yml`) and PyPI publish workflow (`pypi-publish.yml`) to ensure package structure with `__init__.py`.
- Updated `password_generator.py` to fix version inconsistency in header (from 0.2.0 to 0.3.0).
- Updated CI workflow (`python-app.yml`) to add more test cases (no special characters, with ambiguous characters) and additional debugging.
- Updated PyPI publish workflow (`pypi-publish.yml`) to test the built package before publishing.
- Updated PyPI publish workflow (`pypi-publish.yml`) to fix checkout and publish errors by using manual git clone and correcting `packages_dir` parameter.
- Reorganized the `README.md` to separate "Strong Passwords Block I" and "Block II" into distinct sections for CLI usage and examples, improving clarity and usability.
- Updated entropy values in `README.md` to align with recalculated values based on the `password_generator.py` code, ensuring consistency across documentation.
- Modified the CI workflow (`.github/workflows/python-app.yml`) to temporarily adjust the Flake8 command to lint only `password_generator.py`, isolating the source of linting errors during debugging.
- Attempted to apply a custom color (Verde Brilhante 1, #39FF14) to the "Secure by Design" note in the `README.md` under the "Password Entropy Calculation" section using HTML inline styling, but decided against the change due to GitHub Markdown's limited support for custom color rendering.
- Updated the default password length in `password_generator.py` from 66 to 72 characters to align with the expected default maximum length, enhancing the security of generated passwords by default.
- Updated the `--length` argument description in `README.md` under the "CLI Options - Usage Block I" and "CLI Options - Usage Block II" sections to reflect the new default value (`default: 72`), ensuring consistency between the code and documentation.

### Fixed
- Fixed linting errors in `password_generator.py` (Flake8, rule W293) by removing whitespace in blank lines on lines 224, 277, and 293, ensuring the CI/CD pipeline build passes successfully.
- Addressed intermittent CI pipeline failures by confirming the correct version of `password_generator.py` (without whitespace in blank lines) and providing steps to update the repository and clear pipeline cache.

### Removed
- Removed the "Build Status" badge from `README.md` due to persistent linting failures in the CI/CD pipeline, as the issue was related to linting rules rather than functional errors.

## [0.4.0] - 2025-04-27

### Added
- Deep update to the code structure.
- Added version number (0.4.0) to the authorship comment and output header.
- Added `PASSWORDENTROPYCALCULATION.md` document with detailed entropy calculation explanation, benchmarks, and security recommendations.
- Added authorship comment with project information at the beginning of `password_generator.py`.
- Added header with project information (Copyright, Author, GitHub, License, Changelog) in the output of generated passwords.

### Changed
- Updated PyPI publish workflow (`pypi-publish.yml`) to use `actions/checkout@v3` instead of `v4` to resolve persistent checkout error.
- Updated PyPI publish workflow (`pypi-publish.yml`) to fix checkout error by adding event context debugging and `actions:read` permission.
- Updated PyPI publish workflow (`pypi-publish.yml`) with debugging steps to verify Python version, build output, and artifact downloads.
- Updated CI workflow (`python-app.yml`) to use `python -m` for script execution and added debug step to verify working directory.
- Updated CI workflow (`python-app.yml`) to fix script execution by invoking the script directly instead of using `python -m`.
- Refactored `password_generator.py` to fix flake8 linting errors (line length, complexity, spacing).
- Updated minimum Python requirement to 3.8 in `README.md` and `pyproject.toml` due to Python 3.6 deprecation.
- Updated CI workflow (`python-app.yml`) to test with Python 3.8, 3.10, and 3.12, removing Python 3.6.
- Adjusted CLI usage commands in `README.md` to use the package structure (`python -m entropy_password_generator.password_generator`).
- Restructured project as a Python package for PyPI publication, including `pyproject.toml` and package directory.
- Added PyPI publish workflow (`.github/workflows/pypi-publish.yml`) to automatically publish releases.
- Added CI workflow (`.github/workflows/python-app.yml`) for linting and basic script execution across multiple Python versions.
- Adjusted the About section on the project page to fit the 350-character limit while maintaining key details.
- Enhanced the About section on the project page with a more detailed and compelling description of features and benefits.
- Updated entropy values in `README.md` to align with `PASSWORDENTROPYCALCULATION.md` (95.70 bits to 816.64 bits).
- Adjusted link to `PASSWORDENTROPYCALCULATION.md` in `README.md` for clarity.
- Reordered Project Capabilities table in `README.md` by increasing entropy (bits) for better clarity.
- Updated Project Capabilities table in `README.md` with recalculated entropy values for all 20 password generation modes.
- Adjusted separators in the authorship comment for better readability.

## [0.3.0] - 2025-04-25

### Added
- Deep update to the code structure.
- Version number (0.3.0) of the author comment and output header in `password_generator.py`.
- Authorship comment with project information at the beginning of `password_generator.py`.
- Header with project information (Copyright, Author, GitHub, License, Changelog) in the output of generated passwords.

### Changed
- Adjusted separators in the authorship comment for better readability.

## [0.2.0] - 2025-04-24

### Added
- Badges to `README.md` for License (MIT), Language (Python), and Maintenance status.
- `Disclaimer` section to `README.md` with security recommendations (use of password managers and 2FA).

### Changed
- Adjusted `Entropy Calculation` section in `README.md` with new formula notation (`E(R) = log₂(RL)`).
- Reformulated `Contributing` section in `README.md`

---

#### Copyright © 2025 Gerivan Costa dos Santos

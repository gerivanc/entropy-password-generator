# Changelog

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-orange)](https://keepachangelog.com/en/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-blue)](https://semver.org/spec/v2.0.0.html)

All notable changes to the EntroPy Password Generator project are documented in this file. This project adheres to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard, which ensures a structured and human-readable format for tracking changes. By following this approach, we provide clear visibility into the project's evolution, making it easier for users and contributors to understand what has been added, changed, or fixed in each release. Additionally, the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which uses a versioning scheme of MAJOR.MINOR.PATCH. This practice enhances predictability and compatibility by clearly indicating the impact of updates: major versions for breaking changes, minor versions for new features, and patch versions for bug fixes. Together, these standards improve the project's maintainability, transparency, and usability for developers and security enthusiasts.

## [0.4.8] - 2025-05-02

### Added
- Published the `entropy-password-generator` package to the Test Python Package Index (Test PyPI) with version 0.4.7, enabling users to install and test the package via `pip install -i https://test.pypi.org/simple/ entropy-password-generator`. The release is available at [https://test.pypi.org/project/entropy-password-generator/](https://test.pypi.org/project/entropy-password-generator/).
- Added a new section in `README.md` titled "Installation from Test PyPI" with instructions for installing the package from Test PyPI, including the command and a link to the project’s Test PyPI page, improving accessibility for early adopters.
- Added a badge in `README.md` for the Test PyPI release, linking to [https://test.pypi.org/project/entropy-password-generator/](https://test.pypi.org/project/entropy-password-generator/), to highlight the availability of the package and encourage testing.
- Added a verification step in the `pypi-publish.yml` workflow to confirm successful publication to Test PyPI by checking the package’s availability and version on the Test PyPI index, ensuring reliability of the release process.
- Added a note in `SECURITY.md` clarifying that the Test PyPI release is intended for testing purposes and should not be used in production environments, reinforcing security best practices.

### Changed
- Updated the "Usage" section in `README.md` to include an example of running the CLI command (`entropy-password-generator --mode 1`) after installing the package from Test PyPI, ensuring consistency with the new installation method.
- Updated the version number in `pyproject.toml` and `__init__.py` to `0.4.8` to reflect the latest changes and prepare for future releases.
- Enhanced the `pypi-publish.yml` workflow to include a step for generating a release changelog summary for version 0.4.8, extracted from `CHANGELOG.md`, to improve release documentation and visibility.
- Updated the project’s Test PyPI history link in `README.md` to point to [https://test.pypi.org/project/entropy-password-generator/#history](https://test.pypi.org/project/entropy-password-generator/#history), ensuring users can view the release history directly.

### Fixed
- Fixed a minor typo in the `README.md` "Installation from Test PyPI" section, ensuring the pip command uses the correct index URL (`https://test.pypi.org/simple/`) for clarity and accuracy.

## [0.4.7] - 2025-05-01

### Added
- Added a "Visitors" section to `README.md` with a visitor counter badge using the `github-profile-views-counter` service, allowing tracking of repository visits.
- Added an optional "GitHub Stats" section to `README.md` (commented out by default) using `github-readme-stats`, providing a template for displaying GitHub statistics like stars, commits, and contributions.
- Added an explicit `dependencies = []` entry in `pyproject.toml` to clarify that the project has no external dependencies, enhancing transparency for users.
- Added a CLI entry point in `pyproject.toml` under `[project.scripts]` (`entropy-password-generator = "entropy_password_generator.password_generator:main"`), allowing users to run the generator directly via the command `entropy-password-generator` after installation.
- Added a step in `pypi-publish.yml` to clean previous build artifacts (`rm -rf dist/*`) before building the package, preventing potential conflicts during publication.
- Added a caching step for pip dependencies in `pypi-publish 🙂

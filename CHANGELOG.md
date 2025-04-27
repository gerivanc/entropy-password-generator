# Changelog

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-orange)](https://keepachangelog.com/en/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-blue)](https://semver.org/spec/v2.0.0.html)

All notable changes to the EntroPy Password Generator project are documented in this file. This project adheres to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard, which ensures a structured and human-readable format for tracking changes. By following this approach, we provide clear visibility into the project's evolution, making it easier for users and contributors to understand what has been added, changed, or fixed in each release. Additionally, the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which uses a versioning scheme of MAJOR.MINOR.PATCH. This practice enhances predictability and compatibility by clearly indicating the impact of updates: major versions for breaking changes, minor versions for new features, and patch versions for bug fixes. Together, these standards improve the project's maintainability, transparency, and usability for developers and security enthusiasts.

## [Unreleased]

## [0.4.0] - 2025-04-26
### Added
- Version number (0.4.0) Deep update to the code structure.
- Added `EntropyCalculation.md` document with detailed entropy calculation explanation, benchmarks, and security recommendations.

### Changed
- Updated entropy values in `README.md` to align with `EntropyCalculation.md` (95.70 bits to 816.64 bits).
- Adjusted link to `EntropyCalculation.md` in `README.md` for clarity.
- Reordered Project Capabilities table in `README.md` by increasing entropy (bits) for better clarity.
- Updated Project Capabilities table in `README.md` with recalculated entropy values for all 20 password generation modes.
- Adjusted separators in the authorship comment for better readability.
- Added version number (0.2.0) to the authorship comment and output header in password_generator.py.
- Added authorship comment with project information at the beginning of password_generator.py.
- Added header with project information (Copyright, Author, GitHub, License, Changelog) in the output of generated passwords.
- No unreleased changes at the moment.

## [0.3.0] - 2025-04-25
### Added
- Deep update to the code structure.
- Version number (0.3.0) of the author comment and output header in password_generator.py.
- Authorship comment with project information at the beginning of password_generator.py.
- Header with project information (Copyright, Author, GitHub, License, Changelog) in the output of generated passwords.

### Changed
- Adjusted separators in the authorship comment for better readability.
- No unreleased changes at the moment.

## [0.2.0] - 2025-04-24
### Added
- Badges to `README.md` for License (MIT), Language (Python), and Maintenance status.
- `Disclaimer` section to `README.md` with security recommendations (use of password managers and 2FA).

### Changed
- Adjusted `Entropy Calculation` section in `README.md` with new formula notation (`E(R) = log₂(RL)`).
- Reformulated `Contributing` section in `README.md` for clarity ("Want to contribute? Check out our [**Contributing Guidelines**](https://github.com/gerivanc/entropy-password-generator/blob/main/CONTRIBUTING.md)").
- Updated titles in `password_generator.py` from Portuguese to English (`Strong Passwords Block I` and `Block II`).

## [0.1.0] - 2025-04-20
### Added
- Initial project structure with `password_generator.py`, including 20 password generation modes.
- `README.md` with project overview, usage instructions, and examples.
- `CONTRIBUTING.md` with guidelines for contributors.
- `LICENSE.md` with MIT License.

### Changed
- Renamed `CONTRIBUTING.markdown` to `CONTRIBUTING.md` for consistency.
- Removed redundant file `EntroPy Password Generator.markdown`.


#### Copyright © 2025 Gerivan Costa dos Santos

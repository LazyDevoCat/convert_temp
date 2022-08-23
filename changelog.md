# Changelog
All notable changes to this project will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added
- cnagelog.md file with description all versions.
- Issues templates in [GitHub](https://github.com/MariaMaximova/convert_temp/issues/new/choose) page.
- Created unit tests.
- Created validation value type in interactive mode.
- Typing for the returned values in the methods.
- file utils.py with supporting logic.
- simple CI via GitHub Actions.
- file exception.py with extended errors.
- file interactive.py with logic in interactive mode.
- file arguments.py with logic in CLI mode.
- How to use in Readme.md.

### Changed
- Naming of methods.
- decoupling logic from main.py file to two separate files interactive.py and arguments.py.
- Refactoring project structure.

### Fixed
- Some grammatical issues and typos.
- Rounding input.
- Possibility provide the temperature below than absolute zero.


## [1.0.1](https://github.com/MariaMaximova/convert_temp/tree/v1.0.1) - 2022 - August - 10
### Added
- *setup.py* file.
- Added separate folder *converter* within file *converter.py* with all conversion logic.

### Removed
- Convert logic in the main.py file.

### Fixed
- Some grammatical issues and typos.


## [1.0](https://github.com/MariaMaximova/convert_temp/tree/v1.0) - 2022 - August - 06
### Added
- Readme and description were added.
- Create some interactivity.
- Added ability to work with CLI.

### Fixed
- Some grammatical issues and typos

# Changelog for typed-format-version, the format.version.{major,minor} loader

## 0.2.0 (2022-10-02)

- INCOMPATIBLE CHANGE: the Rust implementation's `get_format_from_value()` and
  `get_version_from_value()` functions dropped the "conversion function"
  argument, relying on the "value" argument to implement the `Deserializer`
  trait for its own contents

- Global changes:
  - convert the test data files from JSON to TOML

- Python implementation:
  - drop the flake8 + hacking Tox test environment
  - add both lower and upper version constraints for the dependencies in
    the Tox test environments
  - declare Python 3.11 as a supported version
  - drop `types-dataclasses` from the mypy Tox test environment
  - add a Nix expression for running the Tox tests with different Python
    versions using `nix-shell`
  - add more files to the sdist tarball

- Rust implementation:
  - turn `serde_json` and `serde_yaml` into `dev-dependencies`
  - add `toml` to `dev-dependencies` and run the tests for TOML values, too
  - implement `Eq` for `Version`
  - minor refactoring for some Clippy lints
  - silence the `clippy::std_instead_of_core` lint in the `run-clippy` tool 
  - drop some silenced lints from `run-clippy` since we do not violate them
  - use the `tracing` and `tracing-test` crates for the test suite

## 0.1.0 (2022-07-21)

- First public release.

Contact: [Peter Pentchev](mailto:roam@ringlet.net)

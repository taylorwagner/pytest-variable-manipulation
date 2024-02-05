# Variable Manipulation with Pytest Proof of Concept

This repository is a proof of concept for managing test environments using Pytest and configuration files. It includes functionality for specifying different environments (`dev`, `qa`, `prod`, `testing`, or a custom environment) using the `-E` command-line option and updating a configuration file accordingly.

## Project Structure

- **conftest.py:** Defines the Pytest plugin responsible for handling command-line options and configuring the environment.
  
- **tests/conftest.py:** Contains Pytest fixtures for test data and functions to update, backup, and restore the configuration file.
  
- **tests/variable_test.py:** An example test file that reads a configuration file and prints a variable. You can extend this file with your actual test cases.

- **fixtures/environment.py:** Pytest fixture functions to fetch the environment variable.

- **data/data.ini:** Sample configuration file with a `[DATA]` section containing a placeholder `{environment}` that will be replaced based on the chosen environment.

## Usage

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Install required dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Run the tests with a specified environment:**

    ```bash
    pytest -sv -E=<environment>

## Configuration File

The configuration file, **data/data.ini:**, contains sections and key with values.
The placeholder `{environment}` in the values will be dynamically replaced with the chosen
environment.

## Pytest Fixtures

- environment: Pytest fixture that fetches the values of the 'environment' command-line option.
- env_variable: Pytest fixture that sets the 'env_variable' based on the '-E' command-line option.

## Important Notes

- The original configuration file is backed up before running tests and restored after test execution.
- Ensure that your test cases are appropriately implemented in `variable_test.py` and use the configuration values as needed.

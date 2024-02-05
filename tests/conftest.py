"""Conftest file to define pytest fixtures for test data"""
import os

import pytest
import configparser
import shutil

@pytest.fixture(scope="session")
def environment(request):
    """
    Get the value of the "environment" command-line option from the pytest configuration.

    Args:
        request: Pytest request object.

    Returns:
        str: The value of the "environment" option.

    """
    return request.config.getoption("environment")

def update_ini(config_file, environment):
    """
    Update the values in a configuration file based on the specified environment.

    Args:
        config_file (str): The path to the configuration file.
        environment (str): The environment to substitute in the configuration values.

    """
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(config_file)

    for section in config.sections():
        for key, value in config.items(section):
            updated_value = value.replace('{environment}', environment)
            config[section][key] = updated_value

    with open(config_file, 'w') as configfile:
        config.write(configfile)

def backup_ini(config_file):
    """
    Create a backup of the original INI file.

    Args:
        config_file (str): The path to the configuration file.

    """
    backup_file = config_file + '.backup'
    shutil.copyfile(config_file, backup_file)

def restore_ini(config_file):
    """
    Restore the INI file from the backup.

    Args:
        config_file (str): The path to the configuration file.

    """
    backup_file = config_file + '.backup'
    shutil.move(backup_file, config_file)

def pytest_configure(config):
    """
    Pytest configuration hook to update the configuration file based on the specified environment.

    Args:
        config: Pytest config object.

    """
    environment = config.getoption("environment")
    config_file = 'data/data.ini'
    backup_ini(config_file)
    update_ini(config_file, environment)

def pytest_sessionfinish(session, exitstatus):
    """
    Pytest hook to restore the INI file to its original state after the tests finish.

    Args:
        session: Pytest session object.
        exitstatus: Exit status of the pytest session.

    """
    config_file = 'data/data.ini'
    restore_ini(config_file)
"""Pytest fixture functions"""
import pytest

# Fixture to fetch the environment variable
@pytest.fixture(scope="session", name="env_variable", autouse=True)
def fixture_configure_env_variable_name(request):
    """
    Setting variables based on the 'env' argument
    """
    config_param = {}
    config_param["env_variable"] = request.config.getoption("-E")
    return config_param["env_variable"]
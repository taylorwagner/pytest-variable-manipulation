import pytest

def pytest_addoption(parser):
    """
    Configuring a custom var E (env variable): dev, qa, prod, "", testing
    Throws an error if you pass in a wrong value to 'E' arguments
    """
    print("conftest arguments")
    avail_envs = ["dev", "qa", "prod", "", "testing"]
    parser.addoption(
        "-E",
        dest="environment",
        action="store",
        metavar="NAME",
        default="",
        help="Test environment name.",
    )
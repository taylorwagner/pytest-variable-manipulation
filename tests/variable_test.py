import pytest
import configparser

config = configparser.ConfigParser()
config.read('data/data.ini')

class TestVariableManipulationWithPytestEFlag:

    def test_environment_variables(self):
        print(config['DATA']['TEST'])
        assert 1 == 1
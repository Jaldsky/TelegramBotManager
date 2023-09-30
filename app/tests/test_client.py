from os import path, getcwd
from unittest.case import TestCase

from app.client import Config


class TestConfig(TestCase):
    """Testing the Config class."""

    def test_config(self):
        """Testing loading sensitive data from a file."""
        instance = Config(CONFIG_PATH=path.join(getcwd(), 'app', 'tests', 'test_data', 'config_test_data.ini'))

        self.assertEqual('123456', instance.api_id)
        self.assertEqual('abcdefg1234567', instance.api_hash)
        self.assertEqual('1234567:abcdefg1234567', instance.token1)
        self.assertEqual('7654321:7654321gfedcba', instance.token2)

from os import path, getcwd
from unittest.case import TestCase
from unittest.mock import patch, Mock

from telethon import TelegramClient

from app.bots.cyber_chirik_bot.cyber_chirik_bot import CyberChirikBot
from app.bots.techno_max_bot.techno_max_bot import TechnoMaxBot
from app.client import Config, Client


TEST_FOLDER_DATA = path.join(getcwd(), 'app', 'tests', 'test_data')
TEST_CONFIG_PATH = path.join(TEST_FOLDER_DATA, 'config_test_data.ini')


class TestConfig(TestCase):
    """Testing the Config class."""

    def test_config(self):
        """Testing loading sensitive data from a file."""
        instance = Config(CONFIG_PATH=TEST_CONFIG_PATH)

        self.assertEqual(123456, instance.api_id)
        self.assertEqual('abcdefg1234567', instance.api_hash)
        self.assertEqual('1234567:abcdefg1234567', instance.token1)
        self.assertEqual('7654321:7654321gfedcba', instance.token2)


class ClientMock(Client):
    CONFIG_PATH = TEST_CONFIG_PATH
    BOTS_PATH = TEST_FOLDER_DATA

    def __init__(self, integration: bool = False):
        if integration:
            super().__init__()
        super().__post_init__()


class TestClient(TestCase):
    """Testing the Client class."""

    def setUp(self) -> None:
        self.catch_kwargs = []

    def _catch_input(self, **kwargs):
        if kwargs:
            self.catch_kwargs.append(kwargs)

    def test_client_integration(self):
        """Testing integration with bot calls in a more refined manner."""
        with patch.object(TelegramClient, 'start', new=Mock(side_effect=self._catch_input)):
            with patch.object(CyberChirikBot, 'process', new=Mock(return_value='prc_bot_1')):
                with patch.object(TechnoMaxBot, 'process', new=Mock(return_value='prc_bot_2')):
                    instance = ClientMock(integration=True)

        self.assertEqual(('prc_bot_1', 'prc_bot_2'), instance.bots)
        self.assertEqual(2, len(self.catch_kwargs))

    def test_get_client(self):
        """Testing the method of obtaining a client."""
        instance = ClientMock()
        with patch.object(TelegramClient, '__init__', new=Mock(side_effect=lambda self, arg1, arg2: None)) as mock_init:
            instance.get_client('TestBot')
        result = list(mock_init.call_args)[0]

        self.assertEqual(3, len(result))
        self.assertIn('TestBot', result[0])
        self.assertEqual(instance.api_id, result[1])
        self.assertEqual(instance.api_hash, result[2])

    def test_start_client(self):
        """Testing the method of starting a client."""
        instance = ClientMock()
        with patch.object(TelegramClient, 'start', new=Mock(return_value=None)) as mock:
            instance.start_client('TestBot', '1234567')

        self.assertEqual('1234567', list(mock.call_args)[1]['bot_token'])

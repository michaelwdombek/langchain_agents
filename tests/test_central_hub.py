from unittest import TestCase, mock
from hivemind.central_hub import load_central_hub_config, CentralHub


class TestHiveMindCentralHub(TestCase):
    def test_load_central_hub_config(self):
        # Mock the open function to return a file object
        with mock.patch('builtins.open', mock.mock_open(read_data='{"key": "value"}')) as mock_file:
            # Call the function under test
            config = load_central_hub_config()

            # Assert that the file was opened with the correct path
            mock_file.assert_called_once_with("config/central_hub_defaults.json", "r")

            # Assert that the JSON was loaded correctly
            self.assertEqual(config, {"key": "value"})

    def test_central_hub_default_prompt(self):
        # Create an instance of CentralHub with default values
        central_hub = CentralHub()

        # Assert that the central_prompt is set correctly
        expected_prompt = f"{CentralHub.goal()}\n{CentralHub.structure()}\n{CentralHub.flow()}\n{CentralHub.objective()}"
        self.assertEqual(central_hub.central_prompt, expected_prompt)
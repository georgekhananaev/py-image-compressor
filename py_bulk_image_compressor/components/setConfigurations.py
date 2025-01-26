import os
import configparser

def get_resources() -> configparser.ConfigParser:
    """
    Loads and returns the settings from 'resources/configurations.ini'.
    """
    config = configparser.ConfigParser()

    # Build absolute path to `configurations.ini`
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, '..', 'resources', 'configurations.ini')
    config_path = os.path.abspath(config_path)

    config.read(config_path)
    return config

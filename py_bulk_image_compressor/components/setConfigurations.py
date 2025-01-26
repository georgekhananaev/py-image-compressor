import configparser

def get_resources() -> configparser:
    """
    Loads and returns the settings from 'resources/configurations.ini'.
    """
    my_config = configparser.ConfigParser()
    my_config.read('resources/configurations.ini')
    return my_config
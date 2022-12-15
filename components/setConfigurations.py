import configparser


# passing forward resources parameters from configurations.ini file
def get_resources() -> configparser:
    my_config = configparser.ConfigParser()
    my_config.sections()
    my_config.read('resources/configurations.ini')
    my_config.sections()
    return my_config

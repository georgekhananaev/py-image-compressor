import configparser

def get_resources():
    my_config = configparser.ConfigParser()
    my_config.sections()
    my_config.read('resources/configurations.ini')
    my_config.sections()
    return my_config
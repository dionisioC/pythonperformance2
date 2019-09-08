import configparser


def get_config():
    config_parser = configparser.RawConfigParser()
    config_file_path = r'config.ini'
    config_parser.read(config_file_path)
    return config_parser

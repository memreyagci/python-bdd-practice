import configparser


class ConfigReader:

    def __init__(self):
        self.config_parser = configparser.RawConfigParser()
        config_file_path = "resources/config.properties"
        self.config_parser.read(config_file_path)

    def get_value(self, section, key):
        return self.config_parser.get(section, key)

import json
import os


class ConfigManager():
    def __init__(self, path=os.getcwd()):
        self.config_path = os.path.join(os.path.abspath(path), 'config')

    def read(self):
        with open(self.config_path, 'r') as config_file:
            config = json.load(config_file)

            return config

    def write(self, config=[]):
        default_config = {
            "site_name": "New site"
        }

        default_config.update(config)

        with open(self.config_path, 'w') as config_file:
            json.dump(default_config, config_file)

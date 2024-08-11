import configparser
import os


class Config:
    def __init__(self):
        self.config_parse = configparser.ConfigParser()
        self.config_parse.read('config.ini')
        self.encoding = self.config_parse['SETTINGS']['encoding']


class ConfigSite(Config):
    def __init__(self):
        super().__init__()
        self.link = self.config_parse['SITE']['link']
        self.file_name = self.config_parse['SITE']['file_name']


class ConfigMessenger(Config):
    def __init__(self):
        super().__init__()
        self.vk_token = self.config_parse['VK_API']['vk_token']
        self.vk_id = self.config_parse['VK_API']['vk_id']

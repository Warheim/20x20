import configparser
import os

class Config:
    def __init__(self):
        self.config_parse = configparser.ConfigParser()
        self.config_parse.read('config_management/config.ini')
        self.encoding = self.config_parse['SETTINGS']['encoding']


class ConfigBigSportLoto(Config):
    def __init__(self):
        super().__init__()
        self.link = self.config_parse['SITE_BigSportLoto']['link']
        self.file_name = self.config_parse['SITE_BigSportLoto']['file_name']
        self.main_tag = self.config_parse['PARSER_BigSportLoto']['main_tag']
        self.main_class = self.config_parse['PARSER_BigSportLoto']['main_class']
        self.run_tag = self.config_parse['PARSER_BigSportLoto']['run_tag']
        self.run_class = self.config_parse['PARSER_BigSportLoto']['run_class']
        self.nums_tag = self.config_parse['PARSER_BigSportLoto']['nums_tag']
        self.nums_class = self.config_parse['PARSER_BigSportLoto']['nums_class']


class ConfigMessengers(Config):
    def __init__(self):
        super().__init__()
        self.vk_token = self.config_parse['VK_API']['vk_token']
        self.vk_id = self.config_parse['VK_API']['vk_id']

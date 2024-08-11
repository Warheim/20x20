import configparser


class Config:
    def __init__(self):
        self.config_parse = configparser.ConfigParser()
        self.config_parse.read('config.ini')
        self.encoding = self.config_parse['SETTINGS']['encoding']
        self.file_name = self.config_parse['SITE']['file_name']


class ConfigForSite(Config):
    def __init__(self):
        super().__init__()
        self.link = self.config_parse['SITE']['link']


class ConfigForMessenger(Config):
    def __init__(self):
        super().__init__()
        self.vk_token = self.config_parse['VK_API']['vk_token']
        self.vk_id = self.config_parse['VK_API']['vk_id']


class ConfigForParser(Config):
    def __init__(self):
        super().__init__()
        self.tag = self.config_parse['PARSER']['main_tag']
        self.main_class = self.config_parse['PARSER']['main_class']
        self.run_class = self.config_parse['PARSER']['run_class']
        self.dt_class = self.config_parse['PARSER']['dt_class']
        self.nums_class = self.config_parse['PARSER']['nums_class']

from bs4 import BeautifulSoup
from backend.engine_module.config_management import ConfigBigSportLoto


class ParseArchive(ConfigBigSportLoto):
    def __init__(self):
        super().__init__()

    def soup(self):
        with open(self.file_name, 'r+', encoding=self.encoding) as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        return soup

    def parse(self, soup):
        data = soup.find_all(self.main_tag, class_=self.main_class)
        return data

    def clean_data(self, data):
        clean_data = []
        for run in data:
            run_number = int(run.find(self.run_tag, class_=self.run_class).text)
            nums = run.find_all(self.nums_tag, class_=self.nums_class)
            nums = [int(num.text) for num in nums]
            clean_data.append((run_number, nums[:5], nums[5:]))
        return clean_data

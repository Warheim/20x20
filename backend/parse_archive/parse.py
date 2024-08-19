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
        data = soup.find_all(self.tag, class_=self.main_class)
        return data

    def clean_data(self, data):
        clean_data = []
        for run in data:
            run_number = int(run.find(self.tag,
                                      class_=self.run_class).text.strip())  # TODO They changed design! Re-parse! You stopped here
            print('g')
    #         run_date, run_time = run.find(self.tag, class_=self.dt_class).text.split(' ')
    #         nums = run.find(self.tag, class_=self.nums_class).text.strip().split('\n')
    #         nums = [int(num) for num in nums[:len(nums) // 2] if num.isdigit()]
    #         clean_data.append((run_number, run_date, run_time, nums[:4], nums[4:]))
    #     return clean_data

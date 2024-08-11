import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class DownloadArchive:
    def __init__(self, link, file_name, encoding):
        self.encoding = encoding
        self.link = link
        self.file_name = file_name

        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--start-maximized")

        self.selenium_driver = Chrome(options=self.chrome_options)

    def page_download(self):
        self.selenium_driver.get(self.link)
        with open(f'{os.getcwd().replace('\\', '//')}//..//parse_archive//{self.file_name}', "w",
                  encoding=self.encoding) as file:
            file.write(self.selenium_driver.page_source)
        self.selenium_driver.quit()

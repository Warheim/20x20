import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class DownloadArchive:  # TODO The changed design! Re-load!
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
        old_position = 0
        new_position = None
        while new_position != old_position:
            # Get old scroll position
            old_position = self.selenium_driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
            # Sleep and Scroll
            time.sleep(1)
            self.selenium_driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
            # Get new position
            new_position = self.selenium_driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

        with open(self.file_name, "w", encoding=self.encoding) as file:
            file.write(self.selenium_driver.page_source)
        self.selenium_driver.quit()

from helpers.webdriver_factory import WebdriverFactory
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time


class FakeTyper:
    def __init__(self):
        self.url: str
        self.wd: WebDriver
        self.inputfield: WebElement

    def start(self):
        self.create_webdriver()
        self.run_mainloop()

    def create_webdriver(self):
        self.wd = WebdriverFactory.create(False)

    def run_mainloop(self):
        while True:
            self.setup()
            self.run()
            if not self.run_again():
                break
        self.wd.quit()

    def setup(self):
        while True:
            self.define_url()
            try:
                self.go_to_page()
                self.allow_all_cookies()
                self.define_input()
                break
            except:
                print('probably you are not in a type page')
                pass

    def define_url(self):
        self.url = input('insert the page url to fake type: ')

    def go_to_page(self):
        self.wd.get(self.url)
        time.sleep(5)

    def allow_all_cookies(self):
        if self.is_allow_all_cookies_requested():
            allow_all = self.find_allow_all_cookies_element()
            allow_all.click()
            time.sleep(5)

    def is_allow_all_cookies_requested(self):
        try:
            self.find_allow_all_cookies_element()
            return True
        except:
            return False

    def find_allow_all_cookies_element(self):
        return self.wd.find_element_by_id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    def define_input(self):
        self.inputfield = self.wd.find_element_by_id('inputfield')

    def run(self):
        word_elements = self.get_word_elements()
        for word_element in word_elements:
            word = word_element.text
            self.inputfield.send_keys(word + ' ')

    def get_word_elements(self):
        row: WebElement = self.wd.find_element_by_id('row1')
        return row.find_elements_by_tag_name('span')

    def run_again(self):
        return input('run again (Y: yes): ') == 'Y'

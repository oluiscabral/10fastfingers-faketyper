'''
@author: oluiscabral
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from helpers.webdriver_common import WebdriverCommon

class WebdriverFactory:
    BROWSERS = {
        (webdriver.Chrome, webdriver.ChromeOptions()),
        (webdriver.Firefox, webdriver.FirefoxOptions())
    }
    
    @staticmethod
    def create(headless:bool=True)->WebDriver:
        for browser in WebdriverFactory.BROWSERS:
            try:
                return WebdriverFactory._get_webdriver_to_os(browser[0], browser[1], headless)
            except Exception:
                pass
        raise Exception("Could not find any compatible browser.")
    
    @staticmethod
    def _get_webdriver_to_os(web_driver:WebDriver, options, headless:bool) -> WebDriver:
        if headless:
            options.set_headless()
        ret = web_driver(executable_path=WebdriverCommon.get_path(web_driver), options=options)
        return ret

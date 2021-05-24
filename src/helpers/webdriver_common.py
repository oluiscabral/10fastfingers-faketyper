'''
@author: oluiscabral
'''
from helpers.platform_info import PlatformInfo
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class WebdriverCommon:
    BASE_LOCATION = 'webdrivers'+PlatformInfo.PATH_SEPARATOR
    
    CHROME_LOCATION = BASE_LOCATION+"chromedriver"+PlatformInfo.PATH_SEPARATOR
    GECKO_LOCATION = BASE_LOCATION+"geckodriver"+PlatformInfo.PATH_SEPARATOR
    
    LINUX_FILE = "linux"
    DARWIN_FILE = "darwin"
    WINDOWS_FILE = "win.exe"
    
    @staticmethod
    def get_path(web_driver:WebDriver)->str:
        LOCATION = WebdriverCommon._get_location(web_driver)
        if LOCATION == None or len(LOCATION.strip())==0:
            return None
        PLAT = PlatformInfo.PLATFORM
        if PLAT == 'LINUX' or PLAT == 'LINUX2':
            return WebdriverCommon._build_path(LOCATION, WebdriverCommon.LINUX_FILE)
        elif PLAT == 'DARWIN':
            return WebdriverCommon._build_path(LOCATION, WebdriverCommon.DARWIN_FILE)
        elif PLAT == 'WIN32':
            return WebdriverCommon._build_path(LOCATION, WebdriverCommon.WINDOWS_FILE)
    
    @staticmethod
    def _build_path(LOCATION:str, FILE:str)->str:
        return LOCATION+FILE
    
    @staticmethod
    def _get_location(web_driver:WebDriver)->str:
        if web_driver == webdriver.Chrome:
            return WebdriverCommon.CHROME_LOCATION
        elif web_driver == webdriver.Firefox:
            return WebdriverCommon.GECKO_LOCATION
        return None
    

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.ie.service import Service as IeService
from webdriver_manager.microsoft import IEDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.opera import OperaDriverManager

def get_driver(browser):
    if "chrome" == browser:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    if "firefox" == browser:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    if "edge" == browser:
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    
    if "chromium" == browser:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    
    if "brave" == browser:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    
    if "opera" == browser:
        return webdriver.Opera(executable_path=OperaDriverManager().install())
    
    if "ie" == browser:
        return webdriver.Ie(service=IeService(IEDriverManager().install()))
    
    return


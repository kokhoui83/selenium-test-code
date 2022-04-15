from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriverfactory import get_driver
driver = get_driver("chrome")

driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element(by=By.NAME, value="q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()
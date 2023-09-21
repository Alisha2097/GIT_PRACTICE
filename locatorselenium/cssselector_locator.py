from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class FindElementbyCssSelector():
    def __init__(self):
        pass

    def locate_by_cssselector(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys("test@gmail.com")
        time.sleep(5)

css_selector_locator = FindElementbyCssSelector()
css_selector_locator.locate_by_cssselector()
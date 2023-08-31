from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class FindElementbyXpath():
    def __init__(self):
        pass

    def locate_by_xpath(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys("test@gmail.com")
        time.sleep(5)

xpathlocator = FindElementbyXpath()
xpathlocator.locate_by_xpath()
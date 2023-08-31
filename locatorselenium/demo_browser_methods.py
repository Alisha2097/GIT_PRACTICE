from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

class BrowserMethod():
    def __init__(self):
        pass
    
    @classmethod
    def selenium_method(self):
        driver = webdriver.Chrome()
        driver.get("https://www.rcvacademy.com/")
        print(driver.current_url)
        print(driver.title)

        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()

        # driver.find_element(By.LINK_TEXT,"About").click()
        # driver.back()

        # driver.forward()

        driver.minimize_window()
        time.sleep(5)

method = BrowserMethod()
BrowserMethod.selenium_method()
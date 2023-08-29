from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class DemolocatorByName():
    def __init__(self):
        pass
    def namelocator(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME,"login-input").send_keys("hello@gmail.com")
        time.sleep(5)
findbyname = DemolocatorByName()
findbyname.namelocator()
        
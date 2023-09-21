from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

class Idlocator():
    def __init__(self):
        pass

    def demolocator(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID,"login-continue-btn").click()
        time.sleep(5)

buttonclick = Idlocator()
buttonclick.demolocator()
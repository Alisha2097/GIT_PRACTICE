from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

class Testlocator():
    def __init__(self):
        pass
    @classmethod
    def loactorbyid(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.99.31/en")
        driver.find_element(By.ID,"btn-sign-up").click()
        driver.maximize_window()
        time.sleep(5)

testlocator = Testlocator()
Testlocator.loactorbyid()

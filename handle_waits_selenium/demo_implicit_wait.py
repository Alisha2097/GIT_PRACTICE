from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
import time

class Demo_implicit_wait():
    def implicit_wait(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://login.salesforce.com/?locale=ap")
        driver.find_element(By.ID,"username").send_keys("test@gmail.com")
        driver.find_element(By.ID,"password").send_keys("hellonepal")

   
handle_implicit_wait = Demo_implicit_wait()
handle_implicit_wait.implicit_wait()

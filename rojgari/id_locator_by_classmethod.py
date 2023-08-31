from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class Signin():
    def __init__(self):
        pass

    @classmethod
    def idlocator(self):
        driver= webdriver.Chrome()
        driver.get("http://192.168.99.31/en")
        driver.find_element(By.XPATH,"//a[@class='navbar-item'][normalize-space()='Employer Zone']").click()
        time.sleep(2)
        driver.find_element(By.ID,"btn-sign-up").click()
        driver.find_element(By.ID,"btn-sign-in").click()
        driver.maximize_window()

        time.sleep(5)

signinlocators = Signin()
Signin.idlocator()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

class Signinlocator():
    def __init__(self):
        pass

    def login(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.99.31/en")
        driver.find_element(By.ID,"btn-sign-in").click()
        driver.find_element(By.XPATH,"//input[@placeholder='9841******']").send_keys("8787988787")
        driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']").send_keys("hellonepal")
        driver.find_element(By.ID,"jobSeekerSignInButton").click()
        time.sleep(5)


logintest = Signinlocator()
logintest.login()
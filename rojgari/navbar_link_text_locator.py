from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElementByLinkText():
    def __init__(self) -> None:
        pass

    def linktextlocator(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.99.31/en")
        driver.find_element(By.PARTIAL_LINK_TEXT,"Employer Zo").click()
        time.sleep(2)

linktext = FindElementByLinkText()
linktext.linktextlocator()
    
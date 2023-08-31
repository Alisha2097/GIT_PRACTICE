from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElementByLinkText():
    def __init__(self) -> None:
        pass

    def linktextlocator(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        # driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
        listitem = driver.find_elements(By.TAG_NAME,"a")
        print(len(listitem))
        for list in listitem:
            print(list.text)
        
        time.sleep(5)

linktext = FindElementByLinkText()
linktext.linktextlocator()


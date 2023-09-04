from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

class GetText():
    def __init__(self):
        pass

    def text_of_element(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        text = driver.find_element(By.XPATH,"//span[normalize-space()='Popular domestic Flight Routes']").text
        text1 = driver.find_element(By.LINK_TEXT,"Yatra for Business").text
        
        print(text)
        print(text1)

        time.sleep(5)

gettingtext = GetText()
gettingtext.text_of_element()
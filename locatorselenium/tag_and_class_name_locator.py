from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class FindElementByTagName():
    def __init__(self) -> None:
        pass

    def tagnamelocator(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.find_element(By.TAG_NAME,"input").send_keys("test@gmail.com")
        driver.find_element(By.CLASS_NAME,"email-login-box").send_keys("test@gmail.com")
        time.sleep(4)

tagname = FindElementByTagName()
tagname.tagnamelocator()

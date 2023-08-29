from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
import time


class DemoFindElementByID:
    def __init__(self):
        pass

    #class method 
    def locatebyid(self):
        driver =webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID,"login-input").send_keys('test@test.com')
        time.sleep(5)

#call class method 
findbyid = DemoFindElementByID() #define a variable findbyid 
findbyid.locatebyid() #call method locatebyid()
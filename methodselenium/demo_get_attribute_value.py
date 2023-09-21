from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

class GetAttributeValue():
    def __init__(self):
        pass

    def demo_getvalue(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element(By.ID,"BE_flight_flsearch_btn").get_attribute("value")
        attr_value1 = driver.find_element(By.ID,"BE_flight_flsearch_btn").get_attribute("type")    
        print(attr_value1)
        time.sleep(5)

gettingvalue = GetAttributeValue()
gettingvalue.demo_getvalue()
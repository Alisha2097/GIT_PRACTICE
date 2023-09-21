from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
import time 

class JSExceution():

    def demo_js(self):
        driver = webdriver.Chrome()
        # driver.get("https://training.rcvacademy.com/")
        

        driver.execute_script("window.open('https://training.rcvacademy.com/','_self');")
        driver.maximize_window()
        time.sleep(5)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();",demo_element)

demo_javascript = JSExceution()
demo_javascript.demo_js()
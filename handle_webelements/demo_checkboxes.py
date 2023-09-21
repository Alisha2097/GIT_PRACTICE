from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoCheckbox():

    def checkbox_webelement(self):
        driver = webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.find_element(By.XPATH,"//input[@value='Automation']").click()
        time.sleep(2)

        var1 = driver.find_element(By.XPATH,"//input[@value='Automation']").is_selected()
        print(var1)

        # driver.find_element(By.XPATH,"//input[@value='Performance']").click()
        var2 = driver.find_element(By.XPATH,"//input[@value='Performance']").is_selected()
        print(var2)
        
        driver.maximize_window()
        time.sleep(5)

    def checkbox_webelement1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.find_element(By.XPATH,"//input[@id='profession-1']").click()
        driver.maximize_window()
        time.sleep(5)

    def checkbox_webelement2(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.find_element(By.XPATH,"//input[@value='red']").click()
        driver.maximize_window()
        time.sleep(5)

handle_checkboxes = DemoCheckbox()
handle_checkboxes.checkbox_webelement()
# handle_checkboxes.checkbox_webelement1()
# handle_checkboxes.checkbox_webelement2()
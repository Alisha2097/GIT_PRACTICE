from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoRadiobuttons():

    def radiobtn_webelement(self):
        driver = webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.maximize_window()
        
        var1 = driver.find_element(By.ID,"male").is_selected()
        print(var1)

        driver.find_element(By.ID,"male").click()
        time.sleep(4)

        var2 = driver.find_element(By.ID,"male").is_selected()
        print(var2)

        print(driver.find_element(By.ID,"female").is_selected())
        driver.find_element(By.ID,"female").click()
        time.sleep(4)
        print(driver.find_element(By.ID,"female").is_selected())
        
    def radiobtn_webelement1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.find_element(By.XPATH,"//input[@id='sex-0']").click()
        driver.maximize_window()
        time.sleep(3)

    def radiobtn_webelement2(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.find_element(By.XPATH,"(//input[@name='browser'])[2]").click()
        driver.maximize_window()
        time.sleep(3)

handle_radiobtn = DemoRadiobuttons()
handle_radiobtn.radiobtn_webelement()
# handle_radiobtn.radiobtn_webelement1()
# handle_radiobtn.radiobtn_webelement2()
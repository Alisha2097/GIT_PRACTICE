from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import time

class DemoDropdownSingleSelect():

    def dropdown_webelement(self):
        driver = webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.maximize_window()
        dropdown = driver.find_element(By.XPATH,"//select[@id='testingDropdown']")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_value("Performance")
        time.sleep(3)

        dd.select_by_visible_text("Automation Testing")

        time.sleep(3)

    def dropdown_webelement1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()
        time.sleep(5)
        dropdown1 = driver.find_element(By.XPATH,"//select[@id='continents']")
        dd1 = Select(dropdown1)

        dd1.select_by_index(3)
        time.sleep(3)

        dd1.select_by_visible_text("Europe")
        time.sleep(3)
        
  
handle_dropdown_singleselect = DemoDropdownSingleSelect()
# handle_dropdown_singleselect.dropdown_webelement()
handle_dropdown_singleselect.dropdown_webelement1()

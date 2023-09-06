from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
import time 

class DemoDropdownMultiSelect():

    def multiselect_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        driver.maximize_window()
        #define variable dd_demo
        dd_demo = driver.find_element(By.XPATH,"//select[@id='second']")
        dd_demo.click()
        #define variable dd_multi
        dd_multi = Select(dd_demo)

        dd_multi.select_by_index(0)
        time.sleep(3)
        dd_multi.select_by_index(3)
        time.sleep(3)
        dd_multi.select_by_value("donut")
        time.sleep(3)
        dd_multi.select_by_visible_text("Burger")
        time.sleep(3)

        dd_multi.deselect_by_index(0)
        time.sleep(3)
        dd_multi.deselect_by_visible_text("Blue")
        time.sleep(2)


    def multiselect_dropdown1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
        driver.maximize_window()

        demo_dropdown = driver.find_element(By.XPATH,"//select[@name='selenium_commands']")
        demo_dropdown.click()

        dd_demo = Select(demo_dropdown)
        dd_demo.select_by_index(0)
        time.sleep(3)
        dd_demo.select_by_index(1)
        time.sleep(3)
        dd_demo.select_by_visible_text("WebElement Commands")
        time.sleep(3)

        dd_demo.deselect_by_index(0)
        time.sleep(3)
      
  
handle_dropdown_multiselect = DemoDropdownMultiSelect()
# handle_dropdown_multiselect.multiselect_dropdown()
handle_dropdown_multiselect.multiselect_dropdown1()


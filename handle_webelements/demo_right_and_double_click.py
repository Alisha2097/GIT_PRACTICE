from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
import time

class DemoRightDoubleClick():
    def demo_right_double_click(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        # #Rightclick
        # achains = ActionChains(driver)
        # elem_rc = driver.find_element(By.CLASS_NAME,"context-menu-one")
        # copy_elem = driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        # achains.context_click(elem_rc).perform()
        # time.sleep(2)
        # copy_elem.click()
        # time.sleep(2)

        #Doubleclick
        achains = ActionChains(driver)
        elem_dc = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")
        achains.double_click(elem_dc).perform()
        time.sleep(2)
        
handle_clicks = DemoRightDoubleClick()
handle_clicks.demo_right_double_click()


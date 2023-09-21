from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
import time

class DemoRightDoubleClick():
    def demo_right_double_click(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://nxtgenaiacademy.com/mouseevent/")
        achain = ActionChains(driver)

        #Tooltip(Move the mouse over the text box)
        elemtext = driver.find_element(By.XPATH,"//input[@id='textbox']")
        achain.click(elemtext).send_keys("hello").perform()
        time.sleep(2)

        #Right Click 
        elem1 = driver.find_element(By.XPATH,"//button[@id='rightclick']")
        alert = driver.find_element(By.XPATH,"//a[normalize-space()='Alert Popup']")
        achain.context_click(elem1).perform()
        time.sleep(2)
        alert.click()

        #Double Click 
        elem2 = driver.find_element(By.XPATH,"//button[@id='dblclick']")
        achain.double_click(elem2).perform()
        time.sleep(3)

handle_clicks = DemoRightDoubleClick()
handle_clicks.demo_right_double_click()


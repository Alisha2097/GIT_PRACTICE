from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time 

class DemoJsPopup():

    def demo_js_alerts(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # #Accept Alerts
        driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(3)
    
    def demo_js_confirm(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
        #Dismiss Alerts
        driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
        time.sleep(2)
        # driver.switch_to.alert.accept()
        # time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)
    
    def demo_js_prompt(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        #Send keys
        driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
        time.sleep(5)

        driver.switch_to.alert.send_keys("Hello World")

        driver.switch_to.alert.accept()
        time.sleep(3)

handle_js_alerts = DemoJsPopup()
# handle_js_alerts.demo_js_alerts()
handle_js_alerts.demo_js_confirm()
# handle_js_alerts.demo_js_prompt()
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

class DemoJsPopup():

    def demo_js_alerts(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")

        driver.switch_to.frame("iframeResult")

        # #Accept Alerts
        # driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
        # time.sleep(5)

        # window1 = driver.window_handles
        # print(window1)

        # driver.switch_to.alert.accept()
        # time.sleep(3)

        # #Dismiss Alerts
        # driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
        # time.sleep(2)

        # window = driver.window_handles
        # print(window)

        # driver.switch_to.alert.dismiss()
        # time.sleep(3)

        # #Send keys
        driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
        time.sleep(5)

        driver.switch_to.default_content()

        window3 = driver.window_handles
        print(window3) 

        # driver.switch_to.alert.send_keys("Hello World")

        # window3 = driver.window_handles
        # print(window3) 

        # driver.switch_to.alert.accept()
        # time.sleep(3)

handle_js_alerts = DemoJsPopup()
handle_js_alerts.demo_js_alerts()
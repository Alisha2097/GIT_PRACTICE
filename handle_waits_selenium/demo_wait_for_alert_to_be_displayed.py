from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Demo_waiting_mechanism():
    def demo_expected_conditions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://omayo.blogspot.com/")

        driver.find_element(By.ID,"alert1").click()

        wait = WebDriverWait(driver,5)
        alertbox = wait.until(EC.alert_is_present())

        al = driver.switch_to.alert
        alert_text = al.text
        print(alert_text)
        time.sleep(3)

        al.accept()
       
        time.sleep(3)
       
handle_waits = Demo_waiting_mechanism()
handle_waits.demo_expected_conditions()

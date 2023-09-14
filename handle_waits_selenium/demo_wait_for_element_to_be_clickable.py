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

        driver.find_element(By.XPATH,"//button[normalize-space()='Check this']").click()

        wait = WebDriverWait(driver,12)
        elem2 = wait.until(EC.element_to_be_clickable((By.ID,"dte")))
        elem2.click()

        time.sleep(2)
       
handle_waits = Demo_waiting_mechanism()
handle_waits.demo_expected_conditions()

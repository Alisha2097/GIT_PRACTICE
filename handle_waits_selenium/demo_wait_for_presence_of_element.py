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
        driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()

        wait = WebDriverWait(driver,30)
        elem1 = wait.until(EC.presence_of_element_located((By.ID,"hbutton")))
        hidden_btn_label =elem1.get_attribute("value")
        print(hidden_btn_label)
        
        elem2 =wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Flipkart")))
        elem2.click()

        time.sleep(3)
       
handle_waits = Demo_waiting_mechanism()
handle_waits.demo_expected_conditions()

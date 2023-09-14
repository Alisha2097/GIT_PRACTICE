from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Demo_waiting_mechanism():
    def demo_expected_conditions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        driver.find_element(By.XPATH,"//button[normalize-space()='Start']").click()

        wait = WebDriverWait(driver,10)
        progress_section = wait.until(EC.invisibility_of_element_located((By.ID,"loading")))

        heading_text = driver.find_element(By.ID,"finish").text
        print(heading_text)

        time.sleep(3)
       
handle_waits = Demo_waiting_mechanism()
handle_waits.demo_expected_conditions()

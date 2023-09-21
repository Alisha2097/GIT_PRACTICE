from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WebelementState():

    def element_enable_disable(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()

        demo_state = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo_state)

        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("test@gmail.com")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("test")

        demo_state1 = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo_state1)

        time.sleep(5)

element_status = WebelementState()
element_status.element_enable_disable()
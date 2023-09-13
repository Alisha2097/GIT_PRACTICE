from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class Mouse_Events():
    def mouse_events_demo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://192.168.99.20/")

        register = driver.find_element(By.XPATH,"//a[@class='btn btn-info btn-block rounded custom-register-nav']")

        actions = ActionChains(driver)
        actions.move_to_element(register).click().perform()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,"a[href='#employer_register']").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"//div[@id='employer_register']//a[@class='btn bg-primary text-white w-50'][normalize-space()='Register']").click()
        time.sleep(3)
        
demo_mouse_events = Mouse_Events()
demo_mouse_events.mouse_events_demo()


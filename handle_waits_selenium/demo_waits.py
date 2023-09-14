from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

class Demo_wait():
    def time_sleep_wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://omayo.blogspot.com/")
        driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT,"Facebook").click()
    
    def implicit_wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.implicitly_wait(10) #global wait - applicable for all the web elements present in the automation scripts 

        driver.get("http://omayo.blogspot.com/")
        driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()
        driver.find_element(By.LINK_TEXT,"Facebook").click()

    def explict_wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://omayo.blogspot.com/")
        driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()

        wait = WebDriverWait(driver,10)
        facebookoption = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Facebook")))
        facebookoption.click()
    
    def fluent_wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://omayo.blogspot.com/")
        driver.find_element(By.XPATH,"//button[@class='dropbtn']").click()

        errors = [NoSuchElementException, ElementNotInteractableException]

        wait = WebDriverWait(driver,timeout=10, poll_frequency=2)
        facebookoption = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Facebook")))
        facebookoption.click()
        windowlist = driver.window_handles
        print(windowlist)


handle_waits = Demo_wait()
# handle_waits.time_sleep_wait()
# handle_waits.implicit_wait()
# handle_waits.explict_wait()
handle_waits.fluent_wait()

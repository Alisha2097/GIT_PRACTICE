from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

# Create a new instance of the WebDriver
driver =webdriver.Chrome()

# Navigate to a webpage
driver.get("https://tutorialsninja.com/demo/")

#Maximize Browser
driver.maximize_window()
time.sleep(5)

driver.find_element(By.CLASS_NAME,"fa-search").click()
time.sleep(10)
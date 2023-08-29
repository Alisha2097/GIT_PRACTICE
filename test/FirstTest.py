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

# Find an element by name and Perform actions on the element
driver.find_element(By.NAME,"search").send_keys("iphone")
time.sleep(2)

driver.find_element(By.CLASS_NAME,"fa-search").click()
time.sleep(10)
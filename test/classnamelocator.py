from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

# Create a new instance of the WebDriver
driver =webdriver.Chrome()

# Navigate to a webpage
driver.get("http://omayo.blogspot.com/")

#Maximize Browser
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"dropbtn").click()
time.sleep(5)
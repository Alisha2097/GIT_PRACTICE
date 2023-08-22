from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://tutorialsninja.com/demo/")

# # Find an element by name
# element = driver.find_element(By.NAME, "search")

# # Perform actions on the element
# element.send_keys("iphone")

# # Close the browser
# driver.quit()

# Wait for an element to be visible before performing an action
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.visibility_of_element_located((By.ID, "myElement")))

element = wait.until(EC.visibility_of_element_located((By.NAME, "search")))

# Perform actions on the element
element.send_keys("Iphone")

# Close the browser
driver.quit()

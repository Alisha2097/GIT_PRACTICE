from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://192.168.99.20/")
driver.implicitly_wait(10)

# loginTest
driver.find_element(By.CSS_SELECTOR,".btn.btn-outline-info.btn-block.rounded[href='#']").click()
driver.find_element(By.ID,"id_login").send_keys("client1@gmail.com")
driver.find_element(By.ID,"id_password").send_keys("hellonepal")
driver.find_element(By.ID,"loginBtn").click()

time.sleep(5)
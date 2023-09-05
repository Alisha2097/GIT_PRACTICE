from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HiddenElement():

    def is_displayed_method(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()

        demohiddenelem = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(demohiddenelem)

        driver.find_element(By.CLASS_NAME,"w3-hover-black").click()

        demohiddenelem1 = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(demohiddenelem1)

        time.sleep(5)

    def is_displayed_method_yatra(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH,"//label[@class='travellerLabel']").click()
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        
        elem = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem)

        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        elem1 = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem1)

        driver.maximize_window()
        time.sleep(5)

element_status = HiddenElement()
# element_status.is_displayed_method()
element_status.is_displayed_method_yatra()
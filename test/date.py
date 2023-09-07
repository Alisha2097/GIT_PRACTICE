from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class DatePicker():
    def demo_datepicker(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.automationtesting.in/Datepicker.html")
        driver.find_element(By.XPATH,"//img[@class='imgdp']").click()
        # time.sleep(5)
        # #driver.find_element(By.XPATH,"//a[normalize-space()='21']").click()
        # time.sleep(5)

        all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")
        for dateelement in all_dates:
            date =dateelement.text
            print(date)

            if date == "12":
                dateelement.click()
                break 
            time.sleep(2)
        

handle_datepicker = DatePicker()
handle_datepicker.demo_datepicker()
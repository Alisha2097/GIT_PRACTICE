from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoExplictWait():

    def demo_explict_wait(self):
        driver= webdriver.Chrome()
        driver.get("https://www.yatra.com/")

        depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
       
        depart_from.send_keys("New Delhi")
        
        depart_from.send_keys(Keys.ENTER)
        

        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
       
        search_results = driver.find_elements(By.XPATH,"(//div[@class='viewport'])//div[1]/li")
        print(len(search_results))

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break
        
        wait = WebDriverWait(driver,10)
        flight = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']")))
        flight.click()

        # origin = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        # origin.click()
      

        #to select the date used in framework
        all_dates =driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "12/10/2023":
                date.click()
                break
       
        
handle_explictwait = DemoExplictWait()
handle_explictwait.demo_explict_wait()


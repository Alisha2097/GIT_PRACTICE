from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DemoAutoSuggest():

    def autosuggest_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")

        depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(4)
        search_results = driver.find_elements(By.XPATH,"(//div[@class='viewport'])//div[1]/li")
        print(len(search_results))

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

       
    def autosuggest_dropdown1(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.99.20/")
        autosuggest = driver.find_element(By.XPATH,"//input[@id='job_search'] ")
        autosuggest.click()
        autosuggest.send_keys("Accountant")
        time.sleep(3)
        autosuggest.send_keys(Keys.ENTER)

        
handle_autosuggest = DemoAutoSuggest()
handle_autosuggest.autosuggest_dropdown()
# handle_autosuggest.autosuggest_dropdown1()

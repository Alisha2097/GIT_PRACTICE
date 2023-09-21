from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalenderandDatepicker():

    def calender_webelement(self):
        driver= webdriver.Chrome()
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
                time.sleep(3)
                break

        origin = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        # date = driver.find_element(By.XPATH,"//td[@id='14/09/2023']")
        # date.click()
        # time.sleep(4)

        #to select the date used in framework
        all_dates =driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "12/10/2023":
                date.click()
                time.sleep(5)
                break


handling_calenders = CalenderandDatepicker()
handling_calenders.calender_webelement()
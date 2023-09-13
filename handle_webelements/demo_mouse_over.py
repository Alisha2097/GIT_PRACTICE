from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select
import time

class Demo_Mouse_Over():
    def mouse_events_demo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")

        morebutton = driver.find_element(By.XPATH,"//span[@class='more-arr']")
        myaccount_link = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        achains = ActionChains(driver)
        achains.move_to_element(myaccount_link).click().perform()
        time.sleep(2)
        achains.move_to_element(morebutton).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_xplore']").click()
        time.sleep(2)
        # driver.find_element(By.XPATH,"//a[@id='signInBtn']").click()

handle_mouse_over = Demo_Mouse_Over()
handle_mouse_over.mouse_events_demo()


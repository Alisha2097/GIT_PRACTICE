from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import time

class Register():
    def register_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.99.20/")
        driver.maximize_window()

        driver.find_element(By.XPATH,"//a[@class='btn btn-info btn-block rounded custom-register-nav']").click()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,"div[id='jobseeker_register'] a[class='btn bg-secondary text-white w-50']").click()
        time.sleep(3)

        jobcat_dropdowm = driver.find_element(By.ID,"//div[@class='selectize-input items required has-options full has-items']").click()

job_category = Register()
job_category.register_dropdown()
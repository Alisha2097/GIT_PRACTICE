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

      
        job_categorydd = driver.find_element(By.CLASS_NAME,"selectize-input")
        job_categorydd.click()

        # dd = Select(job_categorydd)

        desired_option_value = "133"
        option_xpath = "//div[normalize-space()='Fashion / Textile Designing']"
        driver.find_element(By.XPATH,option_xpath).click()
        time.sleep(3)

        desired_option_value1 = "212"
        driver.find_element(By.XPATH,"//div[normalize-space()='IT and Telecommunication']").click()
        time.sleep(3)

        # dd.select_by_index(2)
        # time.sleep(3)

        # dd.select_by_value(100)
        # time.sleep(3)

        # dd.select_by_visible_text("Banking / Insurance / Financial Services")
        # time.sleep(3)
       
        
job_category = Register()
job_category.register_dropdown()
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time 

class DemoIframe():

    def demo_frames(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")

        #switch with iframe locator 
        # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

        #switch with name or id 
        driver.switch_to.frame("iframeResult")

        #switch with index
        driver.switch_to.frame(0)

        driver.find_element(By.CLASS_NAME,"tnb-signup-btn").click()
        time.sleep(4)

handle_iframe = DemoIframe()
handle_iframe.demo_frames()
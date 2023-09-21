from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DemoScreenshotCapture():

    def screenshot_capture(self):
        driver= webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        screenshotdemo = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        screenshotdemo.screenshot(".\\test.png")
        screenshotdemo.click()
        time.sleep(2)

        driver.get_screenshot_as_file(".\\error.png")

        driver.save_screenshot(".\\test1.png")

handling_screenshot = DemoScreenshotCapture()
handling_screenshot.screenshot_capture()
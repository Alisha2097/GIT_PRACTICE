from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
import time 

class DemoMultipleWindows():

    def demo_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://nxtgenaiacademy.com/multiplewindows/")
        time.sleep(3)
        driver.maximize_window()

        parent_handle = driver.current_window_handle
        print(parent_handle)

        driver.find_element(By.NAME,"145newbrowsertab234").click()
        time.sleep(5)

        all_handles = driver.window_handles
        print(all_handles)

        for handles in all_handles:
            if handles != parent_handle:
                driver.switch_to.window(handles)
                driver.find_element(By.XPATH,"//div[@class='collapse navbar-collapse pull-right']//a[normalize-space()='Python for Automation']")
                time.sleep(3)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.NAME,"145newbrowsertab234").click()
        time.sleep(2)


handle_multiple_windows = DemoMultipleWindows()
handle_multiple_windows.demo_windows()

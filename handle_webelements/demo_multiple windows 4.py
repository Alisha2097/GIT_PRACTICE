from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time 

class DemoMultipleWindowsQAFox():

    def demo_windows_fox(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://demo.automationtesting.in/Windows.html")
        parentwindow = driver.current_window_handle
        time.sleep(3)
        print("Parent window handle",parentwindow)

        driver.find_element(By.CLASS_NAME,"btn-info").click()
        time.sleep(3)

        child_windows =[]
        child_windows = driver.window_handles
        print("Type of all windows",type(child_windows))

        for child in child_windows:
            print(child)

        driver.switch_to.window(child_windows[1])
        print("Title is:",driver.title)
        driver.find_element(By.CLASS_NAME,"DocSearch-Button").click()
        text1 = driver.find_element(By.XPATH,"//input[@id='docsearch-input']")
        text1.send_keys("selenium")
        time.sleep(5)
        text1.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH,"//a[normalize-space()='Watch the Videos']").click()
        time.sleep(5)

        childwindow = driver.window_handles
        print(childwindow)

        driver.switch_to.window(childwindow[2])
        print("Title is:",driver.title)

        text2 = driver.find_element(By.XPATH,"//input[@id='search']")
        text2.send_keys("Manual Testing")
        text2.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.close()
        time.sleep(5)

        driver.switch_to.window(child_windows[1])
        print("First Child window Title",driver.title)
        driver.close()
        
        driver.switch_to.window(parentwindow)
        print("Parent window Title",driver.title)
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Ram")
        time.sleep(3)

       
handle_multiple_windows = DemoMultipleWindowsQAFox()
handle_multiple_windows.demo_windows_fox()



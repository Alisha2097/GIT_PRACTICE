from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
import time

class DemoSliders():
    def demo_slider_adjustment1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.globalsqa.com/demo-site/sliders/#Color%20Picker")
        time.sleep(2)

        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']"))

        achains = ActionChains(driver)

        elem1 = driver.find_element(By.CSS_SELECTOR,"div[id='red'] span[class='ui-slider-handle ui-corner-all ui-state-default']")
        elem2 = driver.find_element(By.XPATH,"//div[@id='green']//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
        elem3 = driver.find_element(By.XPATH,"//div[@id='blue']//span[@class='ui-slider-handle ui-corner-all ui-state-default']")

        achains.drag_and_drop_by_offset(elem1,-60,0).perform()
        time.sleep(3)

        achains.drag_and_drop_by_offset(elem2,40,0).perform()
        time.sleep(3)

        achains.drag_and_drop_by_offset(elem3,20,0).perform()
        time.sleep(3)

    def demo_slider_adjustment2(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.globalsqa.com/demo-site/sliders/#Range")
        time.sleep(2)

        driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']"))

        achains = ActionChains(driver)

        elem1 = driver.find_element(By.XPATH,"//span[1]")
        elem2 = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > span:nth-child(3)")

        achains.drag_and_drop_by_offset(elem1,60,0).perform()
        time.sleep(3)

        achains.drag_and_drop_by_offset(elem2,-40,0).perform()
        time.sleep(3)

    def demo_slider_adjustment3(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.globalsqa.com/demo-site/sliders/#Steps")
        time.sleep(2)

        driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']"))

        achains = ActionChains(driver)

        elem1 = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
       
        achains.drag_and_drop_by_offset(elem1,70,0).perform()
        time.sleep(3)
      


handle_sliders = DemoSliders()
handle_sliders.demo_slider_adjustment1()
handle_sliders.demo_slider_adjustment2()
handle_sliders.demo_slider_adjustment3()


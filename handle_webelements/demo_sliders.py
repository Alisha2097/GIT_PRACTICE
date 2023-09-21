from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
import time

class DemoSliders():
    def demo_slider_adjustment(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.snapdeal.com/products/automotive-car-interior?sort=plrty#bcrumbLabelId:46106559")

        achains = ActionChains(driver)
        elem1 = driver.find_element(By.CLASS_NAME,"left-handle")
        elem2 = driver.find_element(By.CLASS_NAME,"right-handle")

        achains.drag_and_drop_by_offset(elem1, 60, 0).perform()
        time.sleep(3)
        achains.drag_and_drop_by_offset(elem2, -80, 0).perform()
        time.sleep(3)
        # achains.click_and_hold(elem1).pause(1).move_by_offset(50,0).release().perform()

        # achains.move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80,0).release().perform()
        # time.sleep(3)

   
handle_sliders = DemoSliders()
handle_sliders.demo_slider_adjustment()


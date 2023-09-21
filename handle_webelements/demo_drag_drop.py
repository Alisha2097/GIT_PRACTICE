from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Demo_Drag_Drop():
    def dragdrop_demo1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")

        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))

        achains = ActionChains(driver)

        dragelem = driver.find_element(By.ID,"draggable")
        dropelem = driver.find_element(By.ID,"droppable")

        # achains.drag_and_drop(dragelem,dropelem).perform()
        achains.drag_and_drop_by_offset(dragelem,140,20).perform()
        time.sleep(3)

    def dragdrop_demo2(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager")

        driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']"))

        achains = ActionChains(driver)

        dragelem = driver.find_element(By.XPATH,"//img[@alt='On top of Kozi kopka']")
        dropelem = driver.find_element(By.XPATH,"//div[@id='trash']")

        achains.drag_and_drop(dragelem,dropelem).perform()
       
        time.sleep(3)


handle_drag_drop = Demo_Drag_Drop()
handle_drag_drop.dragdrop_demo1()
handle_drag_drop.dragdrop_demo2()

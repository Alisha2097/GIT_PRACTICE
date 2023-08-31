from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

class FindElementByTagandClassName():
    def __init__(self) -> None:
        pass

    @classmethod
    def classnamelocator(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.99.31/en")
        # driver.find_element(By.TAG_NAME,"input").send_keys("test@gmail.com")
        lista = driver.find_elements(By.TAG_NAME,"small")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(4)

tagname = FindElementByTagandClassName()
FindElementByTagandClassName.classnamelocator()

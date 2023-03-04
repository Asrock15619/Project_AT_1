# invalid Credential:

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_locator import locator
from Test_data import data

class Anup():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self):
        self.driver.get(data.Anup.url)

    
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locator.Anup.username).send_keys(data.Anup.username)
        self.driver.find_element(by=By.NAME,value=locator.Anup.password).send_keys(data.Anup.password)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.loginButton).click()


Anup().login()

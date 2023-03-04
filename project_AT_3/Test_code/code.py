# Add a new employee in PIM Module:

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import Select
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

    def pim(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.PIM).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.add).click()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locator.Anup.firstName).send_keys(data.Anup.firstName)
        self.driver.find_element(by=By.NAME,value=locator.Anup.middleName).send_keys(data.Anup.middleName)
        self.driver.find_element(by=By.NAME,value=locator.Anup.lastName).send_keys(data.Anup.lastName)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.employee).send_keys(data.Anup.employee)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.createlogin).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.user_name).send_keys(data.Anup.user_name)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.pass_word).send_keys(data.Anup.pass__word)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.confirmpassword).send_keys(data.Anup.confirmpassword)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.save).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.gender).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.driving).send_keys(data.Anup.car)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.save).click()


        


Anup().login()

Anup().pim()




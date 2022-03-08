from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyClass:


    def __init__(self, driver):
        self.driver = driver
        self.recollect()

    def recollect(self):
         # self.login = self.driver.find_element_by_xpath(".//div[@id='formsAuthenticationArea']")
         self.header = self.driver.find_element_by_xpath(".//div[@id='header']")

    def get_user_name(self, name):
        login_area = self.driver.find_element_by_xpath(".//div[@id='formsAuthenticationArea']")
        return login_area.find_element_by_xpath\
             (f".//div[@id='userNameArea' or @id='passwordArea']/input[@name='{name}']")

    def click_the_button_in_header(self, name):
        button = self.header.find_element_by_xpath(f".//li[@class='login_links_item']/child::a[text()='{name}']")
        button.click()
        sleep(2)

    def click_the_button(self, name):
        button = self.driver.find_element_by_xpath(f"//div[@id='submissionArea']/span[text()='{name}']")
        button.click()
        sleep(2)
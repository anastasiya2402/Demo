from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyClassLoginLinks:

    def __init__(self, driver):
        self.driver = driver
        self.login_links_in_header()

    def login_links_in_header(self):
        self.login_links = self.driver.find_element_by_xpath("//ul[@id='login_links_list']")
        print(self.login_links.get_attribute('textContent'))
        return self.login_links

    def get_login_link_by_text(self, text):
        return self.login_links.find_element_by_xpath(f".//*[self::li or self::a[text()='{text}']]")


class MyClassHeader:

    def __init__(self, driver):
        self.driver = driver
        self.recollect()

    def recollect(self):
        self.header = self.driver.find_element_by_xpath(".//div[@id='header']")

    def get_user_name(self, name):
        login_area = self.driver.find_element_by_xpath(".//div[@id='formsAuthenticationArea']")
        return login_area.find_element_by_xpath \
            (f".//div[@id='userNameArea' or @id='passwordArea']/input[@name='{name}']")

    def click_the_button_in_header(self, name):
        button = self.header.find_element_by_xpath(f".//li[@class='login_links_item']/child::*[text()='{name}']")
        button.click()
        sleep(2)

    def click_the_button(self, name):
        button = self.driver.find_element_by_xpath(f"//div[@id='submissionArea']/span[text()='{name}']")
        button.click()
        sleep(2)

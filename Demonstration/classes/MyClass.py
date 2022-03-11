from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyClassLoginLinks:

    def __init__(self, driver):
        self.driver = driver
        self.login_links_in_header()

    def login_links_in_header(self):
        self.login_links = self.driver.find_element_by_xpath("//ul[@id='login_links_list']")
        return self.login_links

    def login_links_text(self):
        login_links_list = self.login_links.get_attribute('textContent')
        print(login_links_list)
        return login_links_list

    def get_all_login_elements_in_header(self):
        return self.login_links.find_elements_by_xpath("./li")


class PageBody:

    def __init__(self, driver):
        self.driver = driver
        self.body = self.driver.find_element_by_xpath(".//div[@id='bodyData']")

    def get_all_page_body_data(self):
        return self.body.find_elements_by_xpath(".//ul/li")

class MyClassHeader:

    def __init__(self, driver):
        self.driver = driver
        self.header = self.driver.find_element_by_xpath(".//div[@id='header']")

    def click_the_button_in_header(self, name):
        button = self.header.find_element_by_xpath(f".//li[@class='login_links_item']/child::*[text()='{name}']")
        button.click()
        sleep(2)


class LoginArea:

    def __init__(self, driver):
        self.driver = driver
        self.login_area = self.driver.find_element_by_xpath(".//div[@id='loginArea']")

    def enter_login_credentials(self, name):
        login_credentials = self.login_area.find_element_by_xpath(f".//div[@id='formsAuthenticationArea']"
                                                                  f"/div[@id='userNameArea' or @id='passwordArea']/input[@name='{name}']")
        return login_credentials

    def click_the_button(self, name):
        button = self.login_area.find_element_by_xpath(f".//div[@id='submissionArea']/span[text()='{name}']")
        button.click()
        sleep(2)



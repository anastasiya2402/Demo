from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyClassLoginLinks:

    def __init__(self, driver):
        self.driver = driver
        self.login_links_in_header()

    def login_links_in_header(self):
        self.login_links = self.driver.find_element(by=By.XPATH, value="//ul[@id='login_links_list']")
        return self.login_links

    def login_links_text(self):
        login_links_list = self.login_links.get_attribute('textContent')
        print(login_links_list)
        return login_links_list

    def get_all_login_elements_in_header(self):
        return self.login_links.find_elements(by=By.XPATH, value="./li")


class PageBody:

    def __init__(self, driver):
        self.driver = driver
        self.body = self.driver.find_element(by=By.XPATH, value=".//div[@id='bodyData']")

    def get_all_page_body_data(self):
        return self.body.find_elements(by=By.XPATH, value=".//ul/li")

    def get_body_data_by_text(self, text):
        return self.body.find_element(by=By.XPATH, value=f".//ul/li[starts-with(@class,'gtm_portal_tab') and "
                                                         f"starts-with(text(),'{text}')]")


class MyClassHeader:

    def __init__(self, driver):
        self.driver = driver
        self.header = self.driver.find_element(by=By.XPATH, value=".//div[@id='header']")

    def click_the_button_in_header(self, name):
        button = self.header.find_element(by=By.XPATH,
                                          value=f".//li[@class='login_links_item']/child::*[text()='{name}']")
        button.click()
        sleep(2)


class LoginArea:

    def __init__(self, driver):
        self.driver = driver
        self.login_area = self.driver.find_element(by=By.XPATH, value=".//div[@id='loginArea']")

    def enter_login_credentials(self, name):
        login_credentials = self.login_area.find_element(by=By.XPATH, value=f".//div[@id='formsAuthenticationArea']"
                                                                            f"/div[@id='userNameArea' or @id='passwordArea']/input[@name='{name}']")
        return login_credentials

    def click_the_button(self, name):
        button = self.login_area.find_element(by=By.XPATH, value=f".//div[@id='submissionArea']/span[text()='{name}']")
        button.click()
        sleep(2)


class iFrameRelated:

    def __init__(self, driver):
        self.driver = driver

    def click_link_in_iframe_body(self, text):
        # finding the iframe element
        iframe = self.driver.find_element(by=By.XPATH, value="//iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(by=By.XPATH, value=f"//a[text()='{text}']").click()
        # switching back to the main frame
        self.driver.switch_to.default_content()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_the_button_by_value(self, text, name):
        if self.driver.find_element(by=By.XPATH, value=f"//div[@class='row text-title' and text()='{text}']"):
            button_by_value = self.driver.find_element(by=By.XPATH,
                                                       value=f"//input[@type='button' and @value='{name}']")
            button_by_value.click()
            sleep(2)
        else:
            raise Exception(f'The question {text} should appear')

    def email_box_verification(self, initials):
        return self.driver.find_element(by=By.XPATH,
                                        value="//div[@class='_26RadnUT54i3aZm4ePC1Ws']/child::img")


class PageVisibility:
    def __init__(self, driver):
        self.driver = driver

    def wait_loading(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                  "//*[self::ul[@id='login_links_list'] or self::div[@id='formsAuthenticationArea' or @id='lightbox'"
                                                                                  "or @id='content']]")),
                                             message='Element has not been found')


class WebTables:
    def __init__(self, driver):
        self.driver = driver

    def get_table_by_number(self, number):
        table_by_number = self.driver.find_element(by=By.XPATH, value=
        f"//div[@class='responsive-table']/table[@border='{number}']")
        return table_by_number

    def get_table_row_data(self, number):
        trs = self.get_table_by_number(number).find_elements(by=By.XPATH, value="./tbody/tr")
        row_dict = {}
        for row in trs:
            cells_1 = row.find_element(by=By.XPATH, value="./td[1]")
            cells_2 = row.find_element(by=By.XPATH, value="./td[2]")
            row_dict[cells_1.text] = cells_2.text
        return row_dict


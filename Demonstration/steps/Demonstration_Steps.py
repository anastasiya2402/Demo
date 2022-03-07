from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import step

@step('Navigate to "myut"')
def browser_navigation(context):
    context.browser.get(context.url)


@step('wait for the page to load')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//li[@class='login_links_item']/a[@id='log_btn']")),
        message='Not all elements are visible')


@step('Click on button {name} by text')
def step_impl(context, name):
    button = context.browser.find_element_by_xpath(f"//li[@class='login_links_item']/a[text()='{name}']")
    button.click()
    sleep(2)


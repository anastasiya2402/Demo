from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import step
from Demonstration.classes.MyClass import MyClass

@step('Navigate to "myut"')
def browser_navigation(context):
    context.browser.get(context.url)


@step('wait for the page to load')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//li[@class='login_links_item']/a[@id='log_btn']")),
        message='Not all elements are visible')


@step('Click on button {name} by text in header')
def step_impl(context, name):
    module = MyClass(context.browser)
    module.click_the_button_in_header(name)


@step('Click on button {name} by text')
def step_impl(context, name):
    module = MyClass(context.browser)
    module.click_the_button(name)

@step('Enter {text} into {name}')
def step_impl(context, text, name):
    module = MyClass(context.browser)
    element = module.get_user_name(name)
    ActionChains(context.browser).move_to_element(element).\
        click(on_element=element).send_keys(text).perform()
    sleep(2)

from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import step
from Demonstration.classes.MyClass import *

@step('Navigate to "myut"')
def browser_navigation(context):
    context.browser.get(context.url)


@step('wait for the page to load')
def step_impl(context):
    module = MyClassLoginLinks(context.browser)
    module.login_links_in_header()

@step('Verify that {text} is present')
def step_impl(context, text):
    module = MyClassLoginLinks(context.browser)
    module.get_login_link_by_text(text)




@step('Click on button {name} by text in header')
def step_impl(context, name):
    module = MyClassHeader(context.browser)
    module.click_the_button_in_header(name)


@step('Click on button {name} by text')
def step_impl(context, name):
    module = MyClassHeader(context.browser)
    module.click_the_button(name)

@step('Enter {text} into {name}')
def step_impl(context, text, name):
    module = MyClassHeader(context.browser)
    element = module.get_user_name(name)
    ActionChains(context.browser).move_to_element(element).\
        click(on_element=element).send_keys(text).perform()
    sleep(2)

from selenium import webdriver
import re
from datetime import datetime


def before_all(context):
    context.url = 'http://myut.utoledo.edu/'


# def before_feature(context, feature):
#     context.BASE_URL = f'http://{name}.utoledo.edu/'
#     # store session id
#     context.session = datetime.now().strftime('%d%B_%H_%M.%S')


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(15)
    context.browser.maximize_window()
    context.browser.delete_all_cookies()


def after_step(context, step):
    if step.status == 'failed':
        step_name = re.sub('[^a-zA-Z0-9 \n\.]', '', step.name)
        print(step.name)
        context.browser.save_screenshot(f'{step_name}.png')


def after_scenario(context, scenario):
    context.browser.close()
    context.browser.quit()


# def close_all_tabs_but_first(context):
#     while len(context.browser.window_handles) > 1:
#         context.browser.close()
#         context.browser.switch_to.window(context.browser.window_handles[-1])

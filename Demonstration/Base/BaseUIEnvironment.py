from Demonstration.Base import BaseEnvironment
from Demonstration.Base.BaseEnvironment import *
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Tables_and_Dictionaries.BehaveSupport import item_in_context,\
    context_variable_to_custom_layer,\
    context_delete_variable_from_custom_layer
import logging
# set log level to ERROR for selenium specifically
selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
selenium_logger.setLevel(logging.ERROR)


def init_browser(context=None):
    # import chromedriver_autoinstaller
    # chromedriver_autoinstaller.install()
    # default set to Chrome for now
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("--disable-extensions")
    option.add_argument("--no-sandbox")
    option.add_argument("--window-size=1980,1440")

    # option.add_argument("--kiosk")  # Mac/Linux
    # option.add_argument("--start-maximized")  # Windows

    # option.add_argument("start-maximized")
    # option.add_argument("enable-automation")
    # option.add_argument("--disable-browser-side-navigation")

    # option.add_argument("--headless")
    # option.add_argument("--no-cache")
    # option.add_argument("--dns-prefetch-disable")
    # option.add_argument("--disable-dev-shm-usage")
    #
    # option.add_argument("--disable-gpu")
    # option.add_argument('--lang=en_US')
    # option.add_argument("remote-debugging-port=9222")
    # option.add_argument("--disable-web-security")
    # option.add_argument("--allow-running-insecure-content")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        'download.default_directory': os.path.normpath(os.path.join(os.path.dirname(__file__), "../../")),
        # 'safebrowsing.enabled': False,
    })
    return webdriver.Chrome(chrome_options=option)


def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    context.config.setup_logging()


def before_feature(context, feature):
    # Parent inheritance
    BaseEnvironment.before_feature(context, feature)

    if 'utilize_same_browser_session' in feature.tags:
        # initialize browser and set flag to keep it alive
        context.browser = init_browser(context=context)
        context.keep_browser = True
    else:
        context.keep_browser = False


def before_scenario(context, scenario):
    # Parent inheritance
    BaseEnvironment.before_scenario(context, scenario)

    if 'drop_previous_session' in scenario.tags or \
            ('home_in' in scenario.tags and hasattr(context, 'browser')):
        try:
            context.browser.close()
        except:
            pass
        context.browser.quit()
        context_delete_variable_from_custom_layer(context, 'browser')
        context.browser = init_browser(context=context)

    if 'api' not in scenario.effective_tags:         # no browser needed if scenario is headless
        if not item_in_context(context, 'browser'):  # if browser exists - skip initialization
            context.browser = init_browser(context=context)


def after_step(context, step):
    # attach screenshot to allure report if web step failed
    if step.status == 'failed' and item_in_context(context, 'browser'):
        allure.attach(context.browser.get_screenshot_as_base64(),
                      name=step.name,
                      attachment_type=allure.attachment_type.PNG)

    # Parent inheritance
    BaseEnvironment.after_step(context, step)


def after_scenario(context, scenario):
    """Some tags explanation:

    stay     - with browser reusing to stay on the same page after scenario
    home     - with browser reusing to close all the tabs but first after scenario
    home_out - with browser reusing to drop session after scenario
    home_in  - after scenario to start browser reusing and close all the tabs but first
    """
    # Parent inheritance
    BaseEnvironment.after_scenario(context, scenario)

    # Expected that reuse_browser is not used together with the tags below
    if 'home' in scenario.effective_tags or 'home_in' in scenario.effective_tags:
        close_all_tabs_but_first(context)
        scenario.tags.append('reuse_browser')
    elif 'stay' in scenario.effective_tags:
        scenario.tags.append('reuse_browser')

    if item_in_context(context, 'browser') and\
            'reuse_browser' not in scenario.effective_tags:         # check if driver exists and re-use not planned

        if not context.keep_browser:                                # check the flag
            context.browser.close()
            context.browser.quit()
    elif 'reuse_browser' in scenario.effective_tags:                # make sure browser moved to feature level
        context_variable_to_custom_layer(context, 'browser', context.browser)
    if 'home_out' in scenario.effective_tags:
        context_delete_variable_from_custom_layer(context, 'browser')
    try:
        # flush browser logs
        context.browser.get_log('performance')
    except Exception:
        pass


def after_feature(context, feature):
    # Parent inheritance
    BaseEnvironment.after_feature(context, feature)

    if item_in_context(context, 'browser'):         # close driver if been kept alive
        context.browser.close()
        context.browser.quit()
from behave import step
from Demonstration.classes.MyClass import *
from Tables_and_Dictionaries import BehaveSupport
from Demonstration.Base import ButtonStates
import logging
logger = logging.getLogger('a_shabanskaya')


@step('Navigate to "myut"')
def browser_navigation(context):
    context.browser.get(context.url)


@step('Open "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@step('wait for the page to load')
def step_impl(context):
    module = PageVisibility(context.browser)
    module.wait_loading()


@step('Verify that button {btn_name} is {btn_state}')
def step_impl(context, btn_name, btn_state):
    button = MainMenuButtons(context.browser).get_buttons_in_header(btn_name)
    assert ButtonStates.check_element_state(button, btn_state), f'Button {btn_name} is not {btn_state}'


@step('Verify that {text} is present')
def step_impl(context, text):
    module = MyClassLoginLinks(context.browser)
    assert text in module.login_links_text(), f"Expected name '{text}' is not present!"


@step('Page title should be "{text}"')
def step_impl(context,text):
    """
    Validating the title of the page
    """
    page_title = context.browser.title
    assert text in page_title, f'Title {page_title} is supposed to be {text}.' \
                               f'Current url: {context.browser.current_url}'
    print(context.browser.current_url)
    print(page_title)


@step('Click on button {name} by text in header')
def step_impl(context, name):
    module = MyClassHeader(context.browser)
    module.click_the_button_in_header(name)


@step('Click on button {name} by text')
def step_impl(context, name):
    module = LoginArea(context.browser)
    module.click_the_button(name)


@step('If {text} is asked, then click button "{name}" by value')
def step_impl(context, text, name):
    module = iFrameRelated(context.browser)
    module.click_the_button_by_value(text, name)


@step('Verify that {initials} appears in the upper right corner')
def step_impl(context, initials):
    module = iFrameRelated(context.browser)
    initials_xpath = module.email_box_verification(initials)
    assert initials in initials_xpath.get_attribute('alt'), f'{initials} is not shown or incorrect'


@step('Enter {text} into {name}')
def step_impl(context, text, name):
    module = LoginArea(context.browser)
    element = module.enter_login_credentials(name)
    ActionChains(context.browser).move_to_element(element). \
        click(on_element=element).send_keys(text).perform()
    sleep(2)


@step('Verify that following buttons/links/texts are displayed')
def field_of_type_is_displayed(context):
    step_table = BehaveSupport.table_column_to_list_of_dicts(context.table)
    header = MyClassLoginLinks(context.browser)
    body = PageBody(context.browser)
    for row in step_table:
        if row["Element_type"] == "login-elements-in-header":
            labels = header.get_all_login_elements_in_header()

        elif row["Element_type"] == "body-data-elements":
            labels = body.get_all_page_body_data()

        else:
            raise Exception(f"Not supported type '{row['Element_type']}' for field '{row['Field']}'")

        texts = []
        for label in labels:
            texts.append(label.text)
        assert row["Field"] in texts


@step('Choose tab "{text}"')
def step_impl(context, text):
    module = PageBody(context.browser)
    tab_in_body = module.get_body_data_by_text(text)
    tab_in_body.click()
    sleep(2)


@step('Switch to iframe and go to a new window for {text}')
def step_impl(context, text):
    module = iFrameRelated(context.browser)
    module.click_link_in_iframe_body(text)
    sleep(2)


@step('Verifying table {number} data on the page by comparing two dictionaries')
def step_imp(context, number):
    """

    :param context:
    :param number: the value of @border in the HTML table
    :return:
    """
    step_table = BehaveSupport.table_to_flat_dict(context.table)
    row_dict = WebTables(context.browser).get_table_row_data(number)
    for k, v in step_table.items():
        if k in row_dict.keys():
            assert str(step_table[k]).strip() == str(row_dict[k]).strip(), f'For {k}, expected value is {v},' \
                                                 f' when actual value is {row_dict[k]}'


@step('Verifying table {number} data on the page by comparing two vertical dictionaries consisting of 1st and {j}nd row')
def step_imp(context, number, j):
    """

    :param context:
    :param number: the value of @border in the HTML table
    :return:
    """
    step_table = BehaveSupport.table_columns_to_dicts(context.table)
    print(step_table)
    row_dict = WebTables(context.browser).get_table_column_data(number, j)
    for k, v in step_table.items():
        if k in row_dict.keys():
            assert str(step_table[k]).strip() == str(row_dict[k]).strip(), f'For {k}, expected value is {v},' \
                                                 f' when actual value is {row_dict[k]}'
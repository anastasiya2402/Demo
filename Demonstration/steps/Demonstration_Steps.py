from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import step
from Demonstration.classes.MyClass import *
from Tables_and_Dictionaries import BehaveSupport


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
    assert text in module.login_links_text(), f"Expected name '{text}' is not present!"


@step('Click on button {name} by text in header')
def step_impl(context, name):
    module = MyClassHeader(context.browser)
    module.click_the_button_in_header(name)


@step('Click on button {name} by text')
def step_impl(context, name):
    module = LoginArea(context.browser)
    module.click_the_button(name)


@step('Enter {text} into {name}')
def step_impl(context, text, name):
    module = LoginArea(context.browser)
    element = module.enter_login_credentials(name)
    ActionChains(context.browser).move_to_element(element). \
        click(on_element=element).send_keys(text).perform()
    sleep(2)


@step('Verify that following buttons/links/texts are displayed')
def fieldof_type_is_displayed(context):
    step_table = BehaveSupport.table_column_to_list_of_dicts(context.table)
    header = MyClassLoginLinks(context.browser)
    body = PageBody(context.browser)
    for row in step_table:
        if row["Element_type"] == "login-elements-in-header":
            labels = header.get_all_login_elements_in_header()

        elif row["Element_type"] == "body-data-elements":
            labels = body.get_all_page_body_data()
        #
        # elif row["Element_type"] == "button-group":
        #     labels = proposal_panel.get_all_button_group_labels()
        #
        # elif row["Element_type"] == "date-picker":
        #     labels = proposal_panel.get_all_date_picker_labels()
        #
        # elif row["Element_type"] == "multi-input":
        #     labels = proposal_panel.get_all_multi_inputs_labels()
        #
        # elif row["Element_type"] == "text-area":
        #     labels = proposal_panel.get_all_text_area_labels()
        #
        # elif row["Element_type"] == "required-label":
        #     labels = proposal_panel.get_all_required_labels()
        #
        # elif row["Element_type"] == "checkbox":
        #     labels = proposal_panel.get_all_checkboxes()
        #
        # elif row["Element_type"] == "text-field":
        #     labels = proposal_panel.get_all_text_field_labels()

        else:
            raise Exception(f"Not supported type '{row['Element_type']}' for field '{row['Field']}'")

        texts = []
        for label in labels:
            texts.append(label.text)
        assert row["Field"] in texts
        print(texts)

    # def get_all_dropdowns(self):
    #     return self.find_elements_by_xpath(
    #         ".//div[@class='rc-panel-content']//div[contains(@class, 'select2-container')]" \
    #         "[not(@disabled)][not(ancestor::*[contains(@style, 'display: none')])]")
    #
    # def get_all_dropdown_labels(self):
    #     return self.find_elements_by_xpath(
    #         ".//div[contains(@class, 'select2-container')]/ancestor::div/label")
    #
    # def get_all_input_fields(self):
    #     return self.find_elements_by_xpath(".//div[@class='rc-panel-content']//input[contains(@class, 'text-box')]" \
    #                                        "[not(@disabled)][not(ancestor::*[contains(@style, 'display: none')])]")
    #
    # def get_all_input_labels(self):
    #     return self.find_elements_by_xpath(".//input[contains(@class, 'text-box')]/ancestor::div/label")
    #
    # def get_all_button_groups(self):
    #     return self.find_elements_by_xpath(".//div[@class='rc-panel-content']//div[contains(@class, 'ui-button')]" \
    #                                        "[not(@disabled)][not(ancestor::*[contains(@style, 'display: none')])]")
    #
    # def get_all_button_group_labels(self):
    #     return self.find_elements_by_xpath(".//div[contains(@class, 'ui-button')]/ancestor::div/label")
    #
    # def get_all_multi_inputs(self):
    #     return self.find_elements_by_xpath(
    #         ".//div[@class='rc-panel-content']//div[contains(@class, 'select2-container-multi')]" \
    #         "[not(@disabled)][not(ancestor::*[contains(@style, 'display: none')])]")
    #
    # def get_all_multi_inputs_labels(self):
    #     return self.find_elements_by_xpath(
    #         ".//div[contains(@class, 'select2-container-multi')]/ancestor::div/label")
    #
    # def get_all_date_pickers(self):
    #     return self.find_elements_by_xpath(
    #         ".//div[@class='rc-panel-content']//input[contains(@class, 'text-box-date')]" \
    #         "[not(@disabled)][not(ancestor::*[contains(@style, 'display: none')])]")
    #
    # def get_all_date_picker_labels(self):
    #     return self.find_elements_by_xpath(".//input[contains(@class, 'text-box-date')]/ancestor::div/label")
    #
    # def get_all_text_area_labels(self):
    #     return self.find_elements_by_xpath(".//textarea/ancestor::div/label[contains(@class,'input-label')]")
    #
    # def get_all_text_field_labels(self):
    #     return self.find_elements_by_xpath(".//input[@type='text']/parent::div/label[contains(@class,'input-label')]")
    #
    # def get_all_required_labels(self):
    #     return self.find_elements_by_xpath("//label[contains(@class,'input-label-required')]")
    #
    # def get_all_checkboxes(self):
    #     return self.find_elements_by_xpath("//label/preceding-sibling::input[@type='checkbox']"
    #                                        "/parent::div[@class='checkbutton']")

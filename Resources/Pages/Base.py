import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Locators import Locators
from TestData import TestData


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.delay = 10


    def click(self, by_locator):
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator)).click()


    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text


    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class HomePage(BasePage):
    """Home Page Opencart"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def change_currency_to_euro(self):
        pass

    def change_currency_to_poundsterling(self):
        pass

    def change_currency_to_dollar(self):
        pass

    def contact(self):
        pass

    def click_on_my_account_menu_navbar(self):
        self.click(Locators.MY_ACCOUNT_MENU_NAVBAR)

    def go_to_register_page(self):
        self.click(Locators.MY_ACCOUNT_MENU_NAVBAR)
        self.click(Locators.REGISTER_SUBMENU_NAVBAR)

    def go_to_login_page(self):
        self.click(Locators.LOGIN_SUBMENU_NAVBAR)

    def wishlist(self):
        pass

    def shopping_cart(self):
        pass

    def checkout(self):
        pass

class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_all_fields(self):
        self.enter_text(Locators.FIRST_NAME_TEXT_FIELD, TestData.FIRST_NAME)
        self.enter_text(Locators.LAST_NAME_TEXT_FIELD, TestData.LAST_NAME)
        self.enter_text(Locators.EMAIL_TEXT_FIELD, TestData.EMAIL)
        self.enter_text(Locators.PASSWORD_TEXT_FIELD, TestData.PASSWORD)

    def subscribe_newsletter(self):
        self.click(Locators.NEWSLETTER_SUBSCRIBE_YES_RADIO_BUTTON)

    def read_and_agree(self):
        self.click(Locators.AGREEMENT_CHECK_BOX)
    
    def continue_to_register(self):
        self.click(Locators.CONTINUE_BUTTON)
        time.sleep(5)

    def display_warning_message(self):
        self.assert_element_text(Locators.FIRST_NAME_ERROR_TEXT, TestData.FIRST_NAME_ERROR_MESSAGE)
        self.assert_element_text(Locators.LAST_NAME_ERROR_TEXT, TestData.LAST_NAME_ERROR_MESSAGE)
        self.assert_element_text(Locators.EMAIL_ERROR_TEXT, TestData.EMAIL_ERROR_MESSAGE)
        self.assert_element_text(Locators.PASSWORD_ERROR_TEXT, TestData.PASSWORD_ERROR_MESSAGE)
        self.assert_element_text(Locators.RIGHT_CORNER_ERROR_TEXT, TestData.PRIVACY_POLICY_ERROR_MESSAGE)

    def display_email_registered_warning_message(self):
        self.assert_element_text(Locators.RIGHT_CORNER_ERROR_TEXT, TestData.EMAIL_REGISTERED_ERROR_MESSAGE)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def register_new_customer(self):
        self.click(Locators.GENERAL_CONTINUE_BUTTON)

    def fill_in_all_fields_with_invalid_credentials(self):
        self.enter_text(Locators.EMAIL_TEXT_FIELD, TestData.EMAIL_2)
        self.enter_text(Locators.PASSWORD_TEXT_FIELD, TestData.PASSWORD_2)

    def fill_in_all_fields_with_valid_credentials(self):
        self.enter_text(Locators.EMAIL_TEXT_FIELD, TestData.EMAIL)
        self.enter_text(Locators.PASSWORD_TEXT_FIELD, TestData.PASSWORD)

    def continue_to_login(self):
        self.click(Locators.CONTINUE_BUTTON)
        time.sleep(5)

    def display_failed_credentials_warning_message(self):
        self.assert_element_text(Locators.RIGHT_CORNER_ERROR_TEXT, TestData.INVALID_CREDENTIALS_ERROR_MESSAGE)

class LogoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_home_page(self):
        self.click(Locators.GENERAL_CONTINUE_BUTTON)

class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


class SuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def continue_to_my_account_page(self):
        self.is_visible(Locators.PAGE_TITLE_TEXT)
        self.click(Locators.CONTINUE_BUTTON_AFTER_SUCCESS)

class NewsletterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # def check_default_subscribe_radio_button(self):
    #     self.get_attribute_by_value(Locators.NEWSLETTER_SUBSCRIBE_YES_RADIO_BUTTON)

class MainMenu(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_on_my_account_menu_navbar(self):
        self.click(Locators.MY_ACCOUNT_MENU_NAVBAR)

    def go_to_register_page(self):
        self.click(Locators.MY_ACCOUNT_MENU_NAVBAR)
        self.click(Locators.REGISTER_SUBMENU_NAVBAR)

    def go_to_login_page(self):
        self.click(Locators.LOGIN_SUBMENU_NAVBAR)

    def go_to_logout_page(self):
        self.click(Locators.LOGOUT_SUBMENU_NAVBAR)
        time.sleep(5)


class ActionSection(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_search_field(self):
        self.enter_text(Locators.SEARCH_BAR, TestData.SEARCH_TERM)
    
    def click_on_search_button(self):
        self.click(Locators.SEARCH_BUTTON)


class RightMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_newletter_page_from_right_menu(self):
        self.click(Locators.NEWSLETTER_MENU_RIGHT_NAV)

    def go_to_register_page_from_right_menu(self):
        self.click(Locators.REGISTER_MENU_RIGHT_NAV)

    def go_to_login_page_from_right_menu(self):
        self.click(Locators.LOGIN_MENU_RIGHT_NAV)
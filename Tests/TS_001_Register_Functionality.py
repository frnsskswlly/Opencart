from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner


import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.append("..")
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir+'/Resources')
sys.path.insert(0, parentdir+'/Resources/Pages')

from Locators import Locators
from TestData import TestData
from Pages import Base
from Base import HomePage, LoginPage, MainMenu, NewsletterPage, RegisterPage, RightMenu, SuccessPage

class Test_Register_Functionality_Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.delay = 10

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class Test_Register_Functionality(Test_Register_Functionality_Base):

    def setUp(self):
        super().setUp()

    def test_TC_RF_003_validate_registering_an_account_by_filling_in_all_fields(self):
        self.homePage = HomePage(self.driver)
        self.mainMenu = MainMenu(self.driver)
        self.registerPage = RegisterPage(self.driver)
        self.successPage = SuccessPage(self.driver)

        #
        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()

        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)

        self.registerPage.fill_in_all_fields()
        self.registerPage.read_and_agree()
        self.registerPage.continue_to_register()

        self.assertTrue(TestData.SUCCESS_PAGE_TITLE, self.successPage.driver.title)
        self.successPage.continue_to_my_account_page()
    

    def test_TC_RF_004_validate_registering_an_account_without_filling_in_all_fields(self):
        self.homePage = HomePage(self.driver)
        self.mainMenu = MainMenu(self.driver)
        self.registerPage = RegisterPage(self.driver)

        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()

        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)
        self.registerPage.continue_to_register()
        self.registerPage.display_warning_message()

    # def test_TC_RF_004_validate_registering_an_account_with_subscribing_the_newsletter(self):
    def test_TC_RF_005(self):
        self.homePage = HomePage(self.driver)
        self.mainMenu = MainMenu(self.driver)
        self.registerPage = RegisterPage(self.driver)
        self.rightMenu = RightMenu(self.driver)
        self.successPage = SuccessPage(self.driver)

        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()

        
        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)
        self.registerPage.fill_in_all_fields()
        self.registerPage.subscribe_newsletter()
        self.registerPage.read_and_agree()
        self.registerPage.continue_to_register()

        self.assertTrue(TestData.SUCCESS_PAGE_TITLE, self.successPage.driver.title)
        self.successPage.continue_to_my_account_page()

        self.rightMenu.go_to_newletter_page_from_right_menu()
        self.assertTrue(self.driver.find_element(By.XPATH, '//input[@id = "input-newsletter-yes"]').get_attribute('value'), TestData.RADIOBUTTON_YES_VALUE)

    def test_TC_RF_006(self):
        self.homePage = HomePage(self.driver)
        self.mainMenu = MainMenu(self.driver)
        self.registerPage = RegisterPage(self.driver)
        self.successPage = SuccessPage(self.driver)
        self.rightMenu = RightMenu(self.driver)

        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()


        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)
        self.registerPage.fill_in_all_fields()
        self.registerPage.subscribe_newsletter()
        self.registerPage.read_and_agree()
        self.registerPage.continue_to_register()
        
        self.assertTrue(TestData.SUCCESS_PAGE_TITLE, self.successPage.driver.title)
        self.successPage.continue_to_my_account_page()

        self.rightMenu.go_to_newletter_page_from_right_menu()
        self.assertTrue(self.driver.find_element(By.XPATH, '//input[@id = "input-newsletter-yes"]').get_attribute('value'), TestData.RADIOBUTTON_NO_VALUE)

    def test_TC_RF_007(self):
        self.homePage = HomePage(self.driver)
        self.mainMenu = MainMenu(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.registerPage = RegisterPage(self.driver)
        self.rightMenu = RightMenu(self.driver)
        
        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()
        
        self.assertIn(TestData.LOGIN_PAGE_TITLE, self.loginPage.driver.title)
        self.loginPage.register_new_customer()

        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()

        self.rightMenu.go_to_register_page_from_right_menu()
        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)

    def test_TC_RF_009(self):
        self.homePage = HomePage(self.driver)
        self.mainMenu = MainMenu(self.driver)
        self.registerPage = RegisterPage(self.driver)
        self.successPage = SuccessPage(self.driver)

        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)

        self.mainMenu.click_on_my_account_menu_navbar()
        self.mainMenu.go_to_register_page()

        self.assertIn(TestData.REGISTER_PAGE_TITLE, self.registerPage.driver.title)

        self.registerPage.fill_in_all_fields()
        self.registerPage.read_and_agree()
        self.registerPage.continue_to_register()

        self.registerPage.display_email_registered_warning_message()

    def test_TC_RF_010(self):
        pass

    def test_TC_RF_012(self):
        pass

    def test_TC_RF_013(self):
        pass

    def test_TC_RF_017(self):
        pass

    def test_TC_RF_021(self):
        pass

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/fransiskus/Development/QA Engineer/Selenium + Python/Opencart/Reports'))
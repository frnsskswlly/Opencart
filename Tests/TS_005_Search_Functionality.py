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
from Base import ActionSection, HomePage, LoginPage, LogoutPage, MainMenu, MyAccountPage, NewsletterPage, RegisterPage, RightMenu, SearchResultPage, SuccessPage


class Test_Search_Functionality_Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.delay = 10

        self.homePage = HomePage(self.driver)
        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_Search_Functionality(Test_Search_Functionality_Base):

    def setUp(self):
        super().setUp()

    def test_TC_SF_001(self):
        
        self.actionSection = ActionSection(self.driver)
        
        self.searchResultPage = SearchResultPage(self.driver)

        self.actionSection.fill_in_search_field()
        self.actionSection.click_on_search_button()

        self.searchResultPage.check_search_results()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/fransiskus/Development/QA Engineer/Selenium + Python/Opencart/Reports'))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)


searchButton = driver.find_element(By.XPATH, '//div[@id="search"]//button[@type="button"]')
searchButton.click()

searchPlaceholder = driver.find_element(By.XPATH, '//div[@id="search"]//input[@type="text"]').get_attribute('placeholder')
assert searchPlaceholder == "Search"

searchCriteriaPlaceholder = driver.find_element(By.ID, 'input-search').get_attribute('placeholder')
assert searchCriteriaPlaceholder == "Keywords"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

searchButton = driver.find_element(By.XPATH, '//div[@id="search"]//button[@type="button"]')
searchButton.click()

searchResults = driver.find_elements(By.XPATH, '//h2[contains(text(), "Products meeting the search criteria")]').text

assert searchResults == "Products meeting the search criteria"
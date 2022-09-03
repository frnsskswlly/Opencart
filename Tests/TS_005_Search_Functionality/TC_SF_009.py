from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
search_term = "iMac"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

searchButton = driver.find_element(By.XPATH, '//div[@id = "search"]//button[@type="button"]')
searchButton.click()

searchKeywordText = driver.find_element(By.XPATH, '//input[@id = "input-search"]')
searchKeywordText.send_keys(search_term)

categoryDropdown = driver.find_element(By.XPATH, '//select[@id="input-category"]')
categoryDropdown.click()

categoryOption = driver.find_element(By.XPATH, '//option[@value="27"]')
categoryOption.click()

searchButton2 = driver.find_element(By.XPATH, '//button[@id = "button-search"]')
searchButton2.click()

searchResults = driver.find_element(By.XPATH, '//div[@id="product-list"]//div[@class="description"]//h4')
assert search_term == searchResults.text
# print(searchResults.text)

categoryOption = driver.find_element(By.XPATH, '//option[@value="26"]')
categoryOption.click()

searchButton2 = driver.find_element(By.XPATH, '//button[@id = "button-search"]')
searchButton2.click()

searchResults2 = driver.find_element(By.XPATH, '//p[contains(text(), "There is no product that matches the search criteria.")]')
assert "There is no product that matches the search criteria." == searchResults2.text
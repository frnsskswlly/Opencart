from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
search_term = "Samsung"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

searchText = driver.find_element(By.XPATH, '//input[@type="text"]')
searchText.send_keys(search_term)

searchButton = driver.find_element(By.XPATH, '//div[@id="search"]//button[@type="button"]')
searchButton.click()

searchResults = driver.find_elements(By.XPATH, '//div[@id="product-list"]//div[@class="description"]/h4')
for searchResult in searchResults:
	assert "Samsung" in searchResult.text
	print(searchResult.text)
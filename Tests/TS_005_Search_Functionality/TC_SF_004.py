from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
valid_email = "fransiskuswillywongso@gmail.com"
valid_password = "Dobigthings1289"
search_term = "Samsung"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

loginMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Login")]')
loginMenu.click()

emailText = driver.find_element(By.ID, 'input-email')
emailText.send_keys(valid_email)

passwordText = driver.find_element(By.ID, 'input-password')
passwordText.send_keys(valid_password)

loginButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
loginButton.click()

assert "My Account" in driver.title

searchText = driver.find_element(By.XPATH, '//input[@type="text"]')
searchText.send_keys(search_term)

searchButton = driver.find_element(By.XPATH, '//div[@id="search"]//button[@type="button"]')
searchButton.click()

searchResults = driver.find_elements(By.XPATH, '//div[@id="product-list"]//div[@class="description"]/h4')
for searchResult in searchResults:
	assert "Samsung" in searchResult.text
	print(searchResult.text)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
search_term = "iLife"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

searchButton = driver.find_element(By.XPATH, '//div[@id = "search"]//button[@type="button"]')
searchButton.click()

searchKeywordText = driver.find_element(By.XPATH, '//input[@id = "input-search"]')
searchKeywordText.send_keys(search_term)

searchInProdDescCheckBox = driver.find_element(By.XPATH, '//input[@id="input-description"]')
searchInProdDescCheckBox.click()

searchButton2 = driver.find_element(By.XPATH, '//button[@id = "button-search"]')
searchButton2.click()

searchResults = driver.find_element(By.XPATH, '//div[@id="product-list"]//div[@class="description"]//p')
# assert search_term == searchResults.text
print(searchResults.text)

# cant assert because the text is not containt "iLife", but the whole description is. how?
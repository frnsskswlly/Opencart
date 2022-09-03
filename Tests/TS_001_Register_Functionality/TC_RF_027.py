from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

registerMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Register")]')
registerMenu.click()

assert "Register Account" in driver.title

driver.close()

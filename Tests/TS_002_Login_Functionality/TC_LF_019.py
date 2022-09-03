from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
valid_email = "fransiskuswillywongso@gmail.com"
valid_password = "Dobigthings1289"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

loginMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Login")]')
loginMenu.click()

continueButton = driver.find_element(By.XPATH, '//a[@class = "btn btn-primary"]')
continueButton.click()

driver.back()

newletterRMenu = driver.find_element(By.XPATH, '//a[@class="list-group-item"][contains(text(),"Newsletter")]')
newletterRMenu.click()

driver.close()
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

emailText = driver.find_element(By.ID, 'input-email')
emailText.send_keys(valid_email)

passwordText = driver.find_element(By.ID, 'input-password')
passwordText.send_keys(valid_password)

loginButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
loginButton.click()

myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

logoutMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Logout")]')
logoutMenu.click()

assert "Account Logout" in driver.title

driver.back()
driver.back()

assert "Account Login" in driver.title

driver.close()
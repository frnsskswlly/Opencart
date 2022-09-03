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
emailText.send_keys(Keys.TAB)

passwordText = driver.find_element(By.ID, 'input-password')
passwordText.send_keys(valid_password)
emailText.send_keys(Keys.TAB)

forgotPasswordText = driver.find_element(By.XPATH, '//form[@id="form-login"]//a[contains(text(),"Forgotten Password")]')
forgotPasswordText.send_keys(Keys.TAB)

loginButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
loginButton.send_keys(Keys.RETURN)

assert "My Account" in driver.title

driver.close()
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


# loop for 5 times

i = 0

while i < 1:
	try:
		emailText = driver.find_element(By.ID, 'input-email')
		emailText.clear()
		emailText.send_keys(valid_email)

		passwordText = driver.find_element(By.ID, 'input-password')
		passwordText.clear()
		passwordText.send_keys(valid_password)

		loginButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
		loginButton.click()
	except:
		i = 5

# assert something
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
first_name = "Fransiskus"
last_name = "Willy"
email = "fransiskuswillywongso@gmail.com"
password = "Dobigthings1289"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)
delay = 10


myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

registerMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Register")]')
registerMenu.click()

firstNameText = driver.find_element(By.ID, 'input-firstname').get_attribute('placeholder')
assert firstNameText == "First Name"

lastNameText = driver.find_element(By.ID, 'input-lastname').get_attribute('placeholder')
assert lastNameText == "Last Name"

emailText = driver.find_element(By.ID, 'input-email').get_attribute('placeholder')
assert emailText == "E-Mail Address"

passwordText = driver.find_element(By.ID, 'input-password').get_attribute('placeholder')
assert passwordText == "Password"

driver.close()
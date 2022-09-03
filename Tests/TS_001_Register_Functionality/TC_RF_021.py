from turtle import delay
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

firstNameText = driver.find_element(By.ID, 'input-firstname')
firstNameText.send_keys(first_name)

lastNameText = driver.find_element(By.ID, 'input-lastname')
lastNameText.send_keys(last_name)

emailText = driver.find_element(By.ID, 'input-email')
emailText.send_keys(email)

passwordText = driver.find_element(By.ID, 'input-password')
passwordText.send_keys(password)

continueButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
continueButton.click()

errorAlertText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@id = "alert"]/div[contains(text(), "Warning: You must agree to the Privacy Policy!")]'))).text
print(errorAlertText)

assert errorAlertText == "Warning: You must agree to the Privacy Policy!"

driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
first_name = "Jack"
last_name = "Sparrow"
email = "jacksparrow@gmail.com"
password = "jacksparrow12345"

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

radioButtonYes = driver.find_element(By.ID, 'input-newsletter-yes')
radioButtonYes.click()

agreementCheck = driver.find_element(By.XPATH, '//input[@type = "checkbox"]')
agreementCheck.click()

continueButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
continueButton.click()

errorAlertText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@id = "alert"]/div[contains(text(), "Warning: E-Mail Address is already registered!")]'))).text
print(errorAlertText)

assert errorAlertText == "Warning: E-Mail Address is already registered!"

driver.close()
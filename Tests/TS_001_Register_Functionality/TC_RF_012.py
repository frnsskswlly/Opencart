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
firstNameText.send_keys(Keys.TAB)

lastNameText = driver.find_element(By.ID, 'input-lastname')
lastNameText.send_keys(last_name)
lastNameText.send_keys(Keys.TAB)

emailText = driver.find_element(By.ID, 'input-email')
emailText.send_keys(email)
emailText.send_keys(Keys.TAB)

passwordText = driver.find_element(By.ID, 'input-password')
passwordText.send_keys(password)
passwordText.send_keys(Keys.TAB)

radioButtonYes = driver.find_element(By.ID, 'input-newsletter-yes')
radioButtonYes.send_keys(Keys.ARROW_LEFT)

privacyPolicyText = driver.find_element(By.XPATH, '//b[contains(text(), "Privacy Policy")]')
privacyPolicyText.send_keys(Keys.TAB)

agreementCheck = driver.find_element(By.XPATH, '//input[@type = "checkbox"]')
agreementCheck.send_keys(Keys.SPACE)
agreementCheck.send_keys(Keys.TAB)

continueButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
continueButton.send_keys(Keys.SPACE)

successMessageText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Your Account Has Been Created!")]'))).text

assert successMessageText == "Your Account Has Been Created!"
assert "Your Account Has Been Created!" in driver.title

driver.close()
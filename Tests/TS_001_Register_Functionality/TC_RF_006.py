from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

import time

base_url = "http://localhost/opencart/"
first_name = "Fransiskus"
last_name = "Willy"
email = "fransiskushwillywonxxxgdso@gmail.com"
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

radioButtonNo = driver.find_element(By.ID, 'input-newsletter-no')
radioButtonNo.click()

agreementCheck = driver.find_element(By.XPATH, '//input[@type = "checkbox"]')
agreementCheck.click()

continueButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
continueButton.click()

successMessageText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Your Account Has Been Created!")]'))).text

assert successMessageText == "Your Account Has Been Created!"
assert "Your Account Has Been Created!" in driver.title

continueButton2 = driver.find_element(By.XPATH, '//a[@class = "btn btn-primary"]')
continueButton2.click()

subsUnsubsText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Subscribe / unsubscribe to newsletter")]')))
subsUnsubsText.click()

newsLetterSubsText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Newsletter Subscription")]'))).text

radioButtonNo2 = driver.find_element(By.XPATH, '//input[@id = "input-newsletter-no"]').get_attribute('value')

assert newsLetterSubsText == "Newsletter Subscription"
assert radioButtonNo2 == "1"
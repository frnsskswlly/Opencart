from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

import time

base_url = "https://demo.opencart.com/index.php?route=account/login&language=en-gb"
valid_email = "fransiskuswillywongso@gmail.com"

driver = webdriver.Firefox()
driver.get(base_url)
wait = time.sleep(10)

forgotPasswordText = driver.find_element(By.XPATH, '//form[@id="form-login"]//a[contains(text(),"Forgotten Password")]')
forgotPasswordText.click()


emailText = driver.find_element(By.ID, 'input-email')
emailText.send_keys(valid_email)

continueButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
continueButton.click()

loginButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
loginButton.click()

# assert something
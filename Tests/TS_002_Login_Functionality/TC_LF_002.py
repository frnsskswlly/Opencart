from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"
invalid_email = "fransiskuswillywongsox@gmail.com"
invalid_password = "Dobigthings128910"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)
delay = 10

myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

loginMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Login")]')
loginMenu.click()

emailText = driver.find_element(By.ID, 'input-email')
emailText.send_keys(invalid_email)

passwordText = driver.find_element(By.ID, 'input-password')
passwordText.send_keys(invalid_password)

loginButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
loginButton.click()

errorAlertText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@id = "alert"]/div[contains(text(), "Warning: No match for E-Mail Address and/or Password.")]'))).text
print(errorAlertText)

assert errorAlertText == "Warning: No match for E-Mail Address and/or Password."

driver.close()
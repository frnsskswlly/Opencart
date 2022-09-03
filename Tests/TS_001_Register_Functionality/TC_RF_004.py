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

continueButton = driver.find_element(By.XPATH, '//button[@type = "submit"]')
continueButton.click()

errorFirstNameText = driver.find_element(By.ID, "error-firstname").text
errorLastNameText = driver.find_element(By.ID, "error-lastname").text
errorEmailText = driver.find_element(By.ID, "error-email").text
errorPasswordText = driver.find_element(By.ID, "error-password").text
print(errorFirstNameText)
print(errorLastNameText)
print(errorEmailText)
print(errorPasswordText)

errorAlertText = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@id = "alert"]/div[contains(text(), "Warning: You must agree to the Privacy Policy!")]'))).text
print(errorAlertText)

assert errorFirstNameText == "First Name must be between 1 and 32 characters!"
assert errorLastNameText == "Last Name must be between 1 and 32 characters!"
assert errorEmailText == "E-Mail Address does not appear to be valid!"
assert errorPasswordText == "Password must be between 4 and 20 characters!"
assert errorAlertText == "Warning: You must agree to the Privacy Policy!"

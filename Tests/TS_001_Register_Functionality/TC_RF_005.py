from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

radioButtonYes = driver.find_element(By.ID, 'input-newsletter-yes')
radioButtonYes.click()

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

radioButtonYes2 = driver.find_element(By.XPATH, '//input[@id = "input-newsletter-yes"]').get_attribute('value').text

assert newsLetterSubsText == "Newsletter Subscription"
print(radioButtonYes2)
assert radioButtonYes2.text == "1"
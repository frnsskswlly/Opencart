from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

myAccountMenu = driver.find_element(By.XPATH, '//span[contains(text(), "My Account")]')
myAccountMenu.click()

loginMenu = driver.find_element(By.XPATH, '//a[contains(text(), "Login")]')
loginMenu.click()

forgotPasswordText = driver.find_element(By.XPATH, '//form[@id="form-login"]//a[contains(text(),"Forgotten Password")]')
forgotPasswordText.click()

assert "Forgot Your Password?" in driver.title

driver.close()
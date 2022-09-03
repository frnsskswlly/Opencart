from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


base_url = "https://demo.opencart.com/index.php?route=account/login&language=en-gb"
valid_email = "fransiskuswillywongso@gmail.com"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

forgotPasswordText = driver.find_element(By.XPATH, '//form[@id="form-login"]//a[contains(text(),"Forgotten Password")]')
forgotPasswordText.click()

backButton = driver.find_element(By.XPATH, '//a[@class="btn btn-light"]')
backButton.click()

assert "Account Login" in driver.title

driver.close()
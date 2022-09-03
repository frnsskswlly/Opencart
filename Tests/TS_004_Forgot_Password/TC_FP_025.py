from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "http://localhost/opencart/index.php?route=account/login&language=en-gb"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait(10)

forgotPasswordText = driver.find_element(By.XPATH, '//form[@id="form-login"]//a[contains(text(),"Forgotten Password")]')
forgotPasswordText.click()

assert "Forgot Your Password?" in driver.title
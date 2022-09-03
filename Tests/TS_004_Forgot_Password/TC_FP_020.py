from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "https://demo.opencart.com/index.php?route=account/login&language=en-gb"

driver = webdriver.Firefox()
driver.get(base_url)
driver.implicitly_wait()


newletterRMenu = driver.find_element(By.XPATH, '//a[@class="list-group-item"][contains(text(),"Forgotten Password")]')
newletterRMenu.click()
wait

assert "Forgot Your Password?" in driver.title

driver.close()
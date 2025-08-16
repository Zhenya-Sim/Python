from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

login = driver.find_element(By.CSS_SELECTOR, "#username")
login.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

enter = driver.find_element(By.CSS_SELECTOR, ".radius").click()

print(driver.find_element(By.CSS_SELECTOR, "#flash").text)

driver.quit()

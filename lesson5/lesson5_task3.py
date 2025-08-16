from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

task = driver.find_element(By.CSS_SELECTOR, '[type = "number"]')
task.send_keys("1000")
task.clear()
task.send_keys("999")
driver.quit()

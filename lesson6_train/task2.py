from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "check1")
button.click()

print("Элемент 'Check All' найден и кликнут")

sleep(2)
browser.quit()

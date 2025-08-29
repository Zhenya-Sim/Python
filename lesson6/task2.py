from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")
input = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
input.send_keys("SkyPro")

button = browser.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

txt = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

browser.quit()

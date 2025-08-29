from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get("http://the-internet.herokuapp.com/")

waiter = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "A/B Testing"))
)

print(f"Элемент {waiter.text} найден и виден")

sleep(2)
browser.quit()

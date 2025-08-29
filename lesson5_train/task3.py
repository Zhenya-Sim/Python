from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium")
search_input.send_keys(Keys.RETURN)

sleep(5)

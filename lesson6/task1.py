from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/ajax")
browser.implicitly_wait(17)

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
content = browser.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p[class=bg-success]").text
print(txt)

browser.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


def test_calc():
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    seven = browser.find_element(By.XPATH, "//span[text()='7']")
    seven.click()

    plus = browser.find_element(By.XPATH, "//span[text()='+']")
    plus.click()

    eight = browser.find_element(By.XPATH, "//span[text()='8']")
    eight.click()

    equal = browser.find_element(By.XPATH, "//span[text()='=']")
    equal.click()

    WebDriverWait(browser, 47).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
    WebDriverWait(browser, 47).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    res = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"

    browser.quit()

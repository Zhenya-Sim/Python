from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def window(self):
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def enter_delay(self):
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")

    def enter_numbers(self):
        seven = self._driver.find_element(By.XPATH, "//span[text()='7']")
        seven.click()

        plus = self._driver.find_element(By.XPATH, "//span[text()='+']")
        plus.click()

        eight = self._driver.find_element(By.XPATH, "//span[text()='8']")
        eight.click()

        equal = self._driver.find_element(By.XPATH, "//span[text()='=']")
        equal.click()

    def result(self):
        WebDriverWait(self._driver, 47).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".screen"))).text
        WebDriverWait(self._driver, 47).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))
        res = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res

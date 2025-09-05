from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, browser):
        self._driver = browser
        self.fields = {
            'firstName': "Женя",
            'lastName': "Симонова",
            'postalCode': "443124"
        }

    def open_form(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def fill_form(self):
        for field, value in self.fields.items():
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def continue_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))).click()

    def check_total(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, "finish")))
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div[class='summary_total_label']").text
        total_value = total.split("$")[1]
        return total_value

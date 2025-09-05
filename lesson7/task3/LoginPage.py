from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, browser):
        self._driver = browser
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce"
        }

    def open_shop(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_form(self):
        for field, value in self.fields.items():
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def login(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))).click()

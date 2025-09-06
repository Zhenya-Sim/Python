from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, browser):
        self._driver = browser
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55/3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "Skypro"
        }

    def open_form(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_form(self):
        for field, value in self.fields.items():
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def submit(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    def get_field_class(self, field_id):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    def check_error(self):
        return "alert-danger" in self.get_field_class("zip-code")

    def check_success(self):
        fields = [
            "first-name", "last-name", "address", "city", "country",
            "e-mail", "phone", "job-position", "company"
        ]
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

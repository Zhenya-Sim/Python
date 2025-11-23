from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, browser):
        """
        Конструктор класса LoginPage
        :param browser: WebDriver - объект драйвера Selenium
        :param fields: dict - поля и их значения для заполнения
        """
        self._driver = browser
        self.fields = {
            'user-name': "visual_user",
            'password': "secret_sauce"
        }

    @allure.step("Открытие сайта")
    def open_shop(self):
        """
        Открытие страницы онлайн-магазина
        """
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Авторизация на сайте")
    def fill_form(self):
        """
        Ввод логина и пароля на сайте
        :param field: str - поле для заполнения
        :param value: str - значение для ввода
        """
        for field, value in self.fields.items():
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажатие кнопки Login")
    def login(self):
        """
        Нажатие кнопки Login
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))).click()

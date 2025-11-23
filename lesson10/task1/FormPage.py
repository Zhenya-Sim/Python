from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    def __init__(self, browser):
        """
        Конструктор класса FormPage
        :param browser: WebDriver - объект драйвера Selenium
        """
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

    @allure.step("Открытие сайта с формой")
    def open_form(self):
        """
        Открытие сайта с формой заполнения
        """
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение формы")
    def fill_form(self):
        """
        Заполнение полей формы на сайте
        :param field: str - поле для заполнения
        :param value: str - значение, которое необходимо заполнить
        :param fields: dict - список полей и значений для заполнения
        """
        for field, value in self.fields.items():
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажатие кнопки Submit")
    def submit(self):
        """
        Нажатие кнопки Submit
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Ожидание после заполнения формы {field_id}")
    def get_field_class(self, field_id):
        """
        Ожидание изменения цвета полей после заполнения
        :param field_id: str - название поля в консоли разработчика
        :param element: str - текст для проверки в консоли разработчика
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверка наличия ошибки в незаполненном поле")
    def check_error(self):
        """
        Проверка ошибки в поле Zip-code
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка успешности заполнения остальных полей")
    def check_success(self):
        """
        Проверка корректного заполнения других полей
        :param fields: list - список полей для проверки
        :param field: str - отдельное поле в списке
        """
        fields = [
            "first-name", "last-name", "address", "city", "country",
            "e-mail", "phone", "job-position", "company"
        ]
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

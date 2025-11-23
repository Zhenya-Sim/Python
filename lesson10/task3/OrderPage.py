from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage:
    def __init__(self, browser):
        """
        Конструктор класса OrderPage
        :param browser: WebDriver - объект драйвера Selenium
        :param fields: dict - поля и их значения для заполнения
        """
        self._driver = browser
        self.fields = {
            'firstName': "Женя",
            'lastName': "Симонова",
            'postalCode': "443124"
        }

    @allure.step("Переход на страницу оплаты заказа")
    def open_form(self):
        """
        Открытие страницы оплаты заказа
        """
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Заполнение данных пользователя")
    def fill_form(self):
        """
        Ввод имени, фамилии, индекса пользователя
        :param fields: dict - поля и их значения для заполнения
        :param field: str - поле для заполнения
        :param value: str - значение для ввода
        """
        for field, value in self.fields.items():
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажатие на кнопку Continue")
    def continue_button(self):
        """
        Нажатие на кнопку Continue
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))).click()

    @allure.step("Проверка итоговой суммы")
    def check_total(self):
        """
        Проверка итоговой суммы заказа
        :param total_value: str - сумма заказа
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, "finish")))
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div[class='summary_total_label']").text
        total_value = total.split("$")[1]
        return total_value

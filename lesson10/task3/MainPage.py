from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, browser):
        """
        Конструктор класса MainPage
        Открытие страницы с товарами
        :param browser: WebDriver - объект драйвера Selenium
        """
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/inventory.html")

    @allure.step("Добавление товаров в корзину")
    def add_products(self):
        """
        Добавление товаров в корзину
        """
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход на страницу корзины")
    def go_to_cart(self):
        """
        Нажатие на кнопку перехода в корзину
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, "shopping_cart_container"))).click()

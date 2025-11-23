from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, browser):
        """
        Конструктор класса CartPage
        Открытие страницы с корзиной
        :param browser: WebDriver - объект драйвера Selenium
        """
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Проверка наличия товаров в корзине")
    def get_cart_products(self):
        """
        Проверка наличия ранее выбранных товаров в корзине
        :param product_elements: str - название товара
        """
        product_elements = self._driver.find_elements(
            By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in product_elements]

    @allure.step("Нажатие на кнопку Checkout")
    def button_checkout(self):
        """
        Нажатие на кнопку Checkout (переход на страницу оформления заказа)
        """
        self._driver.find_element(By.ID, "checkout").click()

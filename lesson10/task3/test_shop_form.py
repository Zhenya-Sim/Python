import pytest
from selenium import webdriver
import allure

from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    browser = webdriver.Firefox()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.suite("Тесты на работу онлайн-магазина")
@allure.title("Тестирование онлайн-магазина")
@allure.description("Тест проверяет авторизацию пользователя,"
                    " корректное добавление товаров в корзину,"
                    " возможность оплаты заказа,"
                    " итоговую сумму заказа")
@allure.feature("Выбор и оплата товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(browser):
    """
    Тест проверяет работу онлайн-магазина
    Осуществляется проверка авторизации пользователя,
    Проверка добавления товаров в корзину,
    Отображение выбранных товаров в корзине,
    Проверяется форма заполнения для оплаты заказа,
    Корректная итоговая сумма заказа
    """
    login_page = LoginPage(browser)
    login_page.open_shop()
    login_page.fill_form()
    login_page.login()

    main_page = MainPage(browser)
    main_page.add_products()
    main_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_products = cart_page.get_cart_products()
    expected_products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    with allure.step("Проверка результата"):
        for product in expected_products:
            assert product in cart_products, f"{product} не найден в корзине!"

    order_page = OrderPage(browser)
    order_page.open_form()
    order_page.fill_form()
    order_page.continue_button()
    actual_total = order_page.check_total()
    assert actual_total == '58.29'

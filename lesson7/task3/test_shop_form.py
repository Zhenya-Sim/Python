import pytest
from selenium import webdriver

from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_shop(browser):
    login_page = LoginPage(browser)
    login_page.open_shop()
    login_page.fill_form()
    login_page.login()

    main_page = MainPage(browser)
    main_page.add_products()
    main_page.go_to_cart()

    cart_page = CartPage(browser)
    backpack = cart_page.check_backpack()
    assert backpack == "Sauce Labs Backpack"
    tshirt = cart_page.check_tshirt()
    assert tshirt == "Sauce Labs Bolt T-Shirt"
    onesie = cart_page.check_onesie()
    assert onesie == "Sauce Labs Onesie"
    cart_page.button_checkout()

    order_page = OrderPage(browser)
    order_page.open_form()
    order_page.fill_form()
    order_page.continue_button()
    actual_total = order_page.check_total()
    assert actual_total == '58.29'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/inventory.html")

    def add_products(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, "shopping_cart_container"))).click()

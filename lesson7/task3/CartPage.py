from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/cart.html")

    def check_backpack(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout")))
        backpack = self._driver.find_element(By.ID, "item_4_title_link")
        txt_backpack = backpack.find_element(By.CSS_SELECTOR, 'div').text
        return txt_backpack

    def check_tshirt(self):
        tshirt = self._driver.find_element(By.ID, "item_1_title_link")
        txt_tshirt = tshirt.find_element(By.CSS_SELECTOR, 'div').text
        return txt_tshirt

    def check_onesie(self):
        onesie = self._driver.find_element(By.ID, "item_2_title_link")
        txt_onesie = onesie.find_element(By.CSS_SELECTOR, 'div').text
        return txt_onesie

    def button_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

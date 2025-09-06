from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(options=options)


def test_calc():
    browser.get("https://www.saucedemo.com/")
    browser.implicitly_wait(5)

    login = browser.find_element(By.ID, "user-name")
    login.send_keys("standard_user")
    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    browser.find_element(By.ID, "shopping_cart_container").click()
    browser.find_element(By.ID, "checkout").click()

    f_name = browser.find_element(By.ID, "first-name")
    f_name.send_keys("Женя")
    l_name = browser.find_element(By.ID, "last-name")
    l_name.send_keys("Симонова")
    postal = browser.find_element(By.ID, "postal-code")
    postal.send_keys("443124")

    browser.find_element(By.ID, "continue").click()
    total = browser.find_element(
        By.CSS_SELECTOR, "div[class='summary_total_label']").text
    total_value = float(total.split("$")[1])

    browser.quit()
    assert total_value == 58.29

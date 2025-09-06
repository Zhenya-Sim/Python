import pytest
from selenium import webdriver

from MainPage import MainPage


# def test_search():
#     browser = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()))
#     main_page = MainPage(browser)
#     main_page.window()
#     main_page.search('skypro')

#     sleep(3)
#     browser.quit()


@pytest.fixture()
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()


def test_search(driver):
    page = MainPage(driver)
    page.search_for("Selenium Python")
    results = page.get_search_results()

    assert len(results) > 0, "Результаты поиска не найдены."

# pytest C:\Users\simon\Desktop\Skypro_домашки_и_практика\блок_5_Python\Python\lesson7_train\test_google.py

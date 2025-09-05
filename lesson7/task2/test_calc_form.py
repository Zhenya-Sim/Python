import pytest
from CalcPage import CalcPage
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_calc(browser):
    calc_page = CalcPage(browser)
    calc_page.window()
    calc_page.enter_delay()
    calc_page.enter_numbers()
    calc_page.result()
    result = calc_page.result()
    assert result == '15'

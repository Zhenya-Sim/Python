import pytest
from FormPage import FormPage
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_form(browser):
    form_page = FormPage(browser)
    form_page.open_form()
    form_page.fill_form()
    form_page.submit()
    assert form_page.check_error()
    assert form_page.check_success()

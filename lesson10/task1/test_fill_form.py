import pytest
from FormPage import FormPage
from selenium import webdriver
import allure


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.suite("Тест для проверки формы заполнения")
@allure.title("Тестирование ошибки заполнения поля")
@allure.description("Тест проверяет наличие ошибки"
                    " при незаполнении одного из полей формы")
@allure.feature("Форма заполнения")
@allure.severity(allure.severity_level.CRITICAL)
def test_form(browser):
    """
    Тест осуществляет проверку заполнения формы
    :param driver: WebDriver - объект драйвера из фикстуры
    """
    form_page = FormPage(browser)
    form_page.open_form()
    form_page.fill_form()
    form_page.submit()
    assert form_page.check_error()
    assert form_page.check_success()

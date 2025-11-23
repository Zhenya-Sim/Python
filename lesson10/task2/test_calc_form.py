import pytest
from selenium import webdriver
from CalcPage import CalcPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15),
    ],
)
@allure.suite("Тесты на работу с калькулятором")
@allure.title("Тестирование вычисления {num1} {operation} {num2}"
              " = {expected_result}")
@allure.description("Тест проверяет работу калькулятора "
                    "при операции сложения")
@allure.feature("Калькулятор - сложение")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_flow(driver, num1: str, operation: str,
                         num2: str, expected_result: str, delay: int):
    """
    Тест проверяет работу калькулятора с различными данными
    :param driver: WebDriver - объект драйвера из фикстуры
    :param num1: Первая кнопка для нажатия на калькуляторе
    :param operation: Оператор (+, -, *, /)
    :param num2: Вторая кнопка для нажатия на калькуляторе
    :param expected_result: Ожидаемый результат вычислений
    :param delay: Время задержки выполнения операции (в секундах)
    """
    main_page = CalcPage(driver)

    main_page.open()
    main_page.set_delay(delay)
    main_page.click_buttons([num1, operation, num2, "="])
    main_page.wait_for_result(expected_result, delay)

    with allure.step("Проверка результата"):
        assert main_page.get_result() == expected_result, \
            (f"Expected result:{expected_result}, "
                f"but got:{main_page.get_result()}")

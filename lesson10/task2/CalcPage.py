from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    def __init__(self, driver):
        """
        Конструктор класса CalcPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открытие сайта с онлайн-калькулятором
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html")

    @allure.step("Очистка поля задержки. Установка задержки {delay} сек.")
    def set_delay(self, delay: int):
        """
        Очистка поля ввода задержки вывода результата
        Затем ввод задержки в секундах
        :param delay: время задержки
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопки '{button}' на экране")
    def click_button(self, button: str):
        """
        Этот метод нажимает на одну кнопку калькулятора
        :param button: текст на кнопке калькулятора
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Нажатие кнопок {buttons}")
    def click_buttons(self, buttons: list):
        """
        Нажатие кнопок калькулятора по очереди
        :param buttons: список текстов на кнопках калькулятора
        """
        for button in buttons:
            self.click_button(button)

    @allure.step("Ожидание результата '{expected_result}' на экране")
    def wait_for_result(self, expected_result: str, delay: int):
        """
        Ожидание вывода результата вычислений на экран
        :param expected_result: ожидаемый результат
        :param delay: время задержки
        """
        # Добавляем +1 секунду к задержке для надежности
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self) -> str:
        """
        Возврат результата вычислений с экрана калькулятора
        :param return: полученный результат на экране калькулятора
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text

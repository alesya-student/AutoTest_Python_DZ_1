import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from calculator_page import Calculator


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.epic("Медленный калькулятор.")
@allure.story('Автотест на калькулятор.')
@allure.title('Тест на сложение целых чисел с задержкой вывода результата.')
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    calculator_page = Calculator(browser)
    with allure.step("Выставить ожидание (в сек.)."):
        calculator_page.delay_value(45)
    with allure.step("Нажать на калькуляторе кнопки."):
        calculator_page.click_buttons(["7", "+", "8", "="])
        WebDriverWait(browser, 46).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15'))
    with allure.step("Проверка результата вычисления."):
        result_symbol = calculator_page.get_result_text()
        result = result_symbol
        assert result == '15'
    with allure.step("Вывести результат в консоль"):
        print(f'Значение выражения = {result}')

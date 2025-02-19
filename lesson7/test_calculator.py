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
    yield browser
    browser.quit()


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    calculator_page = Calculator(browser)
    calculator_page.delay_value(45)
    calculator_page.input_symbol(
        symbol_1='//*[@id="calculator"]/div[2]/span[1]',
        symbol_2='//*[@id="calculator"]/div[2]/span[4]',
        symbol_3='//*[@id="calculator"]/div[2]/span[2]',
        symbol_4='//*[@id="calculator"]/div[2]/span[15]'
    )
    WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div.screen'), '15'))

    result_symbol = calculator_page.get_result_text()
    result = result_symbol
    assert result == '15'
    print(f'Значение выражения = {result}')

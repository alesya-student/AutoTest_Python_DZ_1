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


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    calculator_page = Calculator(browser)
    calculator_page.delay_value(45)
    calculator_page.click_buttons(["7", "+", "8", "="])
    WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div.screen'), '15'))

    result_symbol = calculator_page.get_result_text()
    result = result_symbol
    assert result == '15'
    print(f'Значение выражения = {result}')

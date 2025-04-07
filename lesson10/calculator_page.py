import allure
from selenium.webdriver.common.by import By


class Calculator:
    def __init__(self, browser: str):
        self.driver = browser
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html"
                        )

    @allure.step('Меняем значение поля "delay" на значение:{delay}.'
                 'Находим элемент ->'
                 'очищаем текстовое поле -> вводим новые данные'
                 )
    def delay_value(self, delay: int) -> None:
        input_delay = self.driver.find_element(
            By.CSS_SELECTOR, '#delay')  # найти элемент
        input_delay.clear()  # очиcтить текстовое поле
        input_delay.send_keys(delay)  # ввести новые данные

    @allure.step('Нажатие на кнопки {buttons}.')
    def click_buttons(self, buttons) -> None:
        for button in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button}']").click()

    @allure.step('Получение результата.')
    def get_result_text(self) -> str:
        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen')
        return result.text

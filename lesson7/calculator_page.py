from selenium.webdriver.common.by import By


class Calculator:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html"
                        )

#  меняем значение delay ожидания
    def delay_value(self, delay):
        input_delay = self.driver.find_element(
            By.CSS_SELECTOR, '#delay')  # найти элемент
        input_delay.clear()  # очиcтить текстовое поле
        input_delay.send_keys(delay)  # ввести новые данные

    def click_buttons(self, buttons):
        for button in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button}']").click()

    def get_result_text(self):
        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen')
        return result.text

from selenium.webdriver.common.by import By


class Calculator:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

#  меняем значение delay ожидания
    def delay_value(self, delay):
        input_delay = self.driver.find_element(
            By.CSS_SELECTOR, '#delay')  # найти элемент
        input_delay.clear()  # очиcтить текстовое поле
        input_delay.send_keys(delay)  # ввести новые данные

    def input_symbol(self, symbol_1, symbol_2, symbol_3, symbol_4):
        self.driver.find_element(By.XPATH, symbol_1).click()
        self.driver.find_element(By.XPATH, symbol_2).click()
        self.driver.find_element(By.XPATH, symbol_3).click()
        self.driver.find_element(By.XPATH, symbol_4).click()

    def get_result_text(self):
        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen')
        return result.text

import allure
from selenium.webdriver.common.by import By


"""Shop. Оформление покупок:
- ввод данных;
- проверка суммы заказа."""


class Design:
    def __init__(self, browser: str):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Оформление заказа.")
    def checkout(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, '#checkout'
                                 ).location_once_scrolled_into_view
        self.driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    @allure.step("Ввод  личных данных для оформления заказа:"
                 "first_name: {first_name};"
                 "last_name: {last_name}; "
                 "postal_code: {postal_code}."
                 )
    def fill_data(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#continue').click()

# проверка итоговой суммы
    @allure.step("Проверка итоговой суммы.")
    def total_amount(self) -> str:
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.summary_total_label'
                                 ).location_once_scrolled_into_view
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         'div.summary_total_label').text
        return total

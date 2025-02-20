from selenium.webdriver.common.by import By


class Design:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

#  оформление заказа
    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout'
                                 ).location_once_scrolled_into_view
        self.driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    def fill_data(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input#continue').click()

# проверка итоговой суммы
    def total_amount(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.summary_total_label'
                                 ).location_once_scrolled_into_view
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         'div.summary_total_label').text
        return total

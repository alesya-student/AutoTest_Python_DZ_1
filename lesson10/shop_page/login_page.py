import allure
from selenium.webdriver.common.by import By


"""Shop. Страница авторизации"""


class Shop:
    def __init__(self, browser: str):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

#  авторизация
    @allure.step("Авторизация пользователя: {username}:{password}")
    def authorization(self, username: str, password: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, 'input#user-name'
                                 ).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, 'input#password'
                                 ).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'input#login-button'
                                 ).click()

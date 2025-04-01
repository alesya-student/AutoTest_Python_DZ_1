import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Registration:
    def __init__(self, browser: str):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Заполнение формы регистрации.")
    def fill_form(self, first_name: str, last_name: str,
                  address: str, email: str, phone_num: str,
                  zip_code: str, city: str, country: str,
                  job_position: str, company: str) -> None:
        """ Заполняет поля формы регистрации данными."""
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="first-name"]'
                                 ).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="last-name"]'
                                 ).send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="address"]'
                                 ).send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="e-mail"]'
                                 ).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="phone"]'
                                 ).send_keys(phone_num)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="zip-code"]'
                                 ).send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="city"]'
                                 ).send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="country"]'
                                 ).send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="job-position"]'
                                 ).send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'input[name="company"]'
                                 ).send_keys(company)

    @allure.step("Нажатие кнопки 'Submit'.")
    def submit(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn.btn-outline-primary.mt-3").click()

    @allure.step("Проверка цвета элемента (поля).")
    def get_element_by_class(self, id: int) -> str:
        color = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, id))
            ).value_of_css_property('color')
        return color

    @allure.step("Проверка, что незаполненноеполе подсвечено красным.")
    def test_red(self) -> len:

        red_fields = self.driver.find_elements(By.CSS_SELECTOR,
                                               'div.alert.py-2.alert-danger')
        return len(red_fields)

    @allure.step("Проверка, что заполненноеполе подсвечено зеленым.")
    def test_green(self) -> len:
        """Проверка, что заполненноеполе подсвечено зеленым."""
        green_fields = self.driver.find_elements(By.CSS_SELECTOR,
                                                 'div.alert.py-2.alert-success'
                                                 )
        return len(green_fields)

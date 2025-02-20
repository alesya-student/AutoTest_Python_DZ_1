from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Registration:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def fill_form(self, first_name, last_name, address, email, phone_num,
                  zip_code, city, country, job_position, company):
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

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn.btn-outline-primary.mt-3").click()

    def get_element_by_class(self, id):
        color = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, id))
            ).value_of_css_property('color')
        return color

    def test_red(self):
        red_fields = self.driver.find_elements(By.CSS_SELECTOR,
                                               'div.alert.py-2.alert-danger')
        return len(red_fields)

    def test_green(self):
        green_fields = self.driver.find_elements(By.CSS_SELECTOR,
                                                 'div.alert.py-2.alert-success'
                                                 )
        return len(green_fields)

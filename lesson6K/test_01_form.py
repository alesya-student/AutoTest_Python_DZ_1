from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = browser.find_element(By.CSS_SELECTOR,
                                  'input[name="first-name"]')
first_name.clear()
first_name.send_keys('Иван')

last_name = browser.find_element(By.CSS_SELECTOR,
                                 'input[name="last-name"]')
last_name.clear()
last_name.send_keys('Петров')

address = browser.find_element(By.CSS_SELECTOR,
                               'input[name="address"]')
address.clear()
address.send_keys('Ленина, 55-3')

email = browser.find_element(By.CSS_SELECTOR,
                             'input[name="e-mail"]')
email.clear()
email.send_keys('test@skypro.com')

phone_num = browser.find_element(By.CSS_SELECTOR,
                                 'input[name="phone"]')
phone_num.clear()
phone_num.send_keys('+7985899998787')

phone_num = browser.find_element(By.CSS_SELECTOR,
                                 'input[name="phone"]')
phone_num.clear()
phone_num.send_keys('+7985899998787')

zip_code = browser.find_element(By.CSS_SELECTOR,
                                'input[name="zip-code"]')
zip_code.clear()

city = browser.find_element(By.CSS_SELECTOR,
                            'input[name="city"]')
city.clear()
city.send_keys('Москва')

country = browser.find_element(By.CSS_SELECTOR,
                               'input[name="country"]')
country.clear()
country.send_keys('Россия')

job_position = browser.find_element(By.CSS_SELECTOR,
                                    'input[name="job-position"]')
job_position.clear()
job_position.send_keys('QA')

company = browser.find_element(By.CSS_SELECTOR,
                               'input[name="company"]')
company.clear()
company.send_keys('SkyPro')

submit = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,
                                      'button.btn.btn-outline-primary.mt-3'))
    ).click()

zip_code_red = browser.find_element(By.CSS_SELECTOR,
                                    'div#zip-code').get_attribute('class')
assert 'alert-danger'
print(zip_code_red)

green_fields = browser.find_elements(By.CSS_SELECTOR,
                                     'div.alert.py-2.alert-success')
assert len(green_fields) == 9
print(len(green_fields))

browser.quit()

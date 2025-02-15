from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

input_num = browser.find_element(By.CSS_SELECTOR, '#delay')
input_num.clear()
input_num.send_keys('45')

browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

wait = WebDriverWait(browser, 46)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'),
                                            '15'))

result = browser.find_element(By.CSS_SELECTOR, 'div.screen').text
assert result == '15'
print(result)

browser.quit()

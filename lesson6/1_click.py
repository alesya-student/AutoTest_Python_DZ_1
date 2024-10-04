from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService
                           (ChromeDriverManager().install()))
browser.implicitly_wait(16)

browser.get('http://uitestingplayground.com/ajax')

browser.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

# content = WebDriverWait(browser, 15).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR,'#content'))
# )

content = browser.find_element(By.CSS_SELECTOR, '#content')

info = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(f'текст: {info}')

browser.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService
                           (ChromeDriverManager().install()))

browser.implicitly_wait(20)

browser.get('http://uitestingplayground.com/textinput')

input = browser.find_element(By.CSS_SELECTOR, '#newButtonName')
input.send_keys('SkyPro')

browser.find_element(By.CSS_SELECTOR, '#updatingButton').click()

txt = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
# newButton = browser.find_element(By.CSS_SELECTOR, '#newButtonName')

print(txt)

WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#updatingButton'),
                                     'SkyPro'))

browser.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = Options()
driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

driver.find_element(By.CSS_SELECTOR, 'div.modal-footer').click()
sleep(2)


driver.quit()

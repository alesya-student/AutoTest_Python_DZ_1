from time import sleep
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


# firefox_options = Options()
driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/login')


username = driver.find_element(By.ID, 'username')
username.send_keys('tomsmith')
sleep(2)


password = driver.find_element(By.ID, 'password')
password.send_keys('SuperSecretPassword!h')
sleep(2)


driver.find_element(By.CSS_SELECTOR, '.radius').click()
sleep(2)


driver.quit()

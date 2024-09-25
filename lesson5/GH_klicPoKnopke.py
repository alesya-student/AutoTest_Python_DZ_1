from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


for i in range(5):
    driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()


buttonDelete = driver.find_elements(By.XPATH, ("//button[text()='Delete']"))
print(f'Количество кнопок DELETE: {len(buttonDelete)}')


sleep(5)

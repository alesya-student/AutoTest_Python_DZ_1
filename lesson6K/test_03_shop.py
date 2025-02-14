from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

#  авторизация
username = browser.find_element(By.CSS_SELECTOR, 'input#user-name'
                                ).send_keys('standard_user')
password = browser.find_element(By.CSS_SELECTOR, 'input#password'
                                ).send_keys('secret_sauce')
login = browser.find_element(By.CSS_SELECTOR, 'input#login-button'
                             ).click()

#  добавление товара в корзину
product_1 = browser.find_element(By.CSS_SELECTOR,
                                 'button#add-to-cart-sauce-labs-backpack'
                                 ).click()
product_2 = browser.find_element(By.CSS_SELECTOR,
                                 'button#add-to-cart-sauce-labs-bolt-t-shirt'
                                 ).click()
scroll_product_3 = browser.find_element(By.CSS_SELECTOR,
                                        '#add-to-cart-sauce-labs-onesie')
scroll_product_3.location_once_scrolled_into_view
product_3 = browser.find_element(By.CSS_SELECTOR,
                                 'button#add-to-cart-sauce-labs-onesie'
                                 ).click()

#  переход в корзину
scroll_container = browser.find_element(By.CSS_SELECTOR,
                                        '#shopping_cart_container')
scroll_container.location_once_scrolled_into_view
container = browser.find_element(By.CSS_SELECTOR,
                                 'div#shopping_cart_container').click()

#  оформление заказа
scroll_checkout = browser.find_element(By.CSS_SELECTOR, '#checkout')
scroll_checkout.location_once_scrolled_into_view
checkout = browser.find_element(By.CSS_SELECTOR, 'button#checkout').click()

first_name = browser.find_element(By.CSS_SELECTOR,
                                  'input#first-name').send_keys('Alesya')
last_name = browser.find_element(By.CSS_SELECTOR,
                                 'input#last-name').send_keys('Vasina')
last_name = browser.find_element(By.CSS_SELECTOR,
                                 'input#postal-code').send_keys('603000')
click_continue = browser.find_element(By.CSS_SELECTOR,
                                      'input#continue').click()

# проверка итоговой суммы
scroll_total = browser.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
scroll_total.location_once_scrolled_into_view
total = browser.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
print(total)

assert total == 'Total: $58.29'

browser.quit()

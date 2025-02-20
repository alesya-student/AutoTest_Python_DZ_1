from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

#  добавление товара в корзину
    def product_in_cart(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button#add-to-cart-sauce-labs-backpack'
                                 ).click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button#add-to-cart-sauce-labs-bolt-t-shirt'
                                 ).click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#add-to-cart-sauce-labs-onesie'
                                 ).location_once_scrolled_into_view
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button#add-to-cart-sauce-labs-onesie'
                                 ).click()

#  переход в корзину
    def to_go_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container'
                                 ).location_once_scrolled_into_view
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div#shopping_cart_container').click()

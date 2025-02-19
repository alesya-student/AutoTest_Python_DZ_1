import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from shop_page.login_page import Shop
from shop_page.cart_page import Cart
from shop_page.productDesign_page import Design


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    login_page = Shop(browser)
    login_page.authorization(
        username='standard_user',
        password='secret_sauce'
    )
    cart_page = Cart(browser)
    cart_page.product_in_cart()
    cart_page.to_go_cart()
    productDesign_page = Design(browser)
    productDesign_page.checkout()
    productDesign_page.fill_data(
        first_name='Alesya',
        last_name='Vasina',
        postal_code='603000'
    )
    total_sum = productDesign_page.total_amount()
    assert total_sum == 'Total: $58.29'

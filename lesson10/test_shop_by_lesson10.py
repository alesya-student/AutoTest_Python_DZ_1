import allure
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


@allure.epic("Интернет-магазин.")
@allure.story('Автотест на оформления покупки.')
@allure.title('Тест на прохождение цикла "оформление покупки до оплаты".')
@allure.severity(allure.severity_level.BLOCKER)
def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    login_page = Shop(browser)
    with allure.step("Авторизоваться."):
        login_page.authorization(
            username='standard_user',
            password='secret_sauce'
        )
    with allure.step("Добавить товары в корзину."):
        cart_page = Cart(browser)
        cart_page.product_in_cart()
    with allure.step("Перейти в корзину (иконка корзины вверху справа)."):
        cart_page.to_go_cart()
        productDesign_page = Design(browser)
    with allure.step("Нажать 'Сheckout'"):
        productDesign_page.checkout()
    with allure.step("Ввести данные для оформления заказа"):
        productDesign_page.fill_data(
            first_name='Alesya',
            last_name='Vasina',
            postal_code='603000'
            )
    with allure.step("Проверить, что итоговая сумма равна,"
                     "сумме стоимсотивыбранныз заказов"):
        total_sum = productDesign_page.total_amount()
        assert total_sum == 'Total: $58.29'

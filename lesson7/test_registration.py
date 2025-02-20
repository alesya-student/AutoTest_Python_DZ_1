import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from registration_page import Registration


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


#  Тест 1. Заполнение формы.
def test_card_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    registration_page = Registration(browser)
    registration_page.fill_form(
        first_name='Иван',
        last_name='Петров',
        address='Ленина, 55-3',
        email='test@skypro.com',
        phone_num='+7985899998787',
        zip_code='',
        city='Москва',
        country='Россия',
        job_position='QA',
        company='SkyPro'
    )

    registration_page.submit()
    print('Форма заполнена!')


#  Тест 2. Соответствие id поля и цвета поля.
def test_color_field():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    registration_page = Registration(browser)
    registration_page.fill_form(
        first_name='Иван',
        last_name='Петров',
        address='Ленина, 55-3',
        email='test@skypro.com',
        phone_num='+7985899998787',
        zip_code='',
        city='Москва',
        country='Россия',
        job_position='QA',
        company='SkyPro'
    )

    registration_page.submit()

    #  возможно проверить любое поле, подставляя id и цвет на соответствие
    #  rgba(132, 32, 41, 1) - красный
    #  rgba(15, 81, 50, 1) - зеленый
    attribute_color = registration_page.get_element_by_class('#zip-code')
    assert attribute_color == 'rgba(132, 32, 41, 1)'
    print(f'поле "Zip code" атрибут color: {attribute_color}')


#  Тест 3. Количество полей определенного класса.
#  class = *alert-danger - не заполненное поле
#  class = *alert-success - заполненное поле
def test_class():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    registration_page = Registration(browser)
    registration_page.fill_form(
        first_name='Иван',
        last_name='Петров',
        address='Ленина, 55-3',
        email='test@skypro.com',
        phone_num='+7985899998787',
        zip_code='',
        city='Москва',
        country='Россия',
        job_position='QA',
        company='SkyPro'
    )

    registration_page.submit()

    class_alert_danger = registration_page.test_red()
    assert class_alert_danger == 1
    print(f'Количество полей класс "alert-danger": {class_alert_danger}')

    class_alert_success = registration_page.test_green()
    assert class_alert_success == 9
    print(f'Количество полей класс "alert-success": {class_alert_success}')

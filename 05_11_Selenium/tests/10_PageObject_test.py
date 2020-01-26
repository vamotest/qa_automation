from page_objects.user_page import UserPage
from page_objects.user_login import UserLogin
from page_objects.breadcrumbs import BreadCrumbs
from page_objects.header import Header
from page_objects.search_page import SearchPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage

import yaml
import pytest

conf = yaml.safe_load(open('configuration.yml'))

email = conf['user']['email']
password = conf['user']['password']


def test_login_user(browser):
    """
    Проверка авторизации пользователя в личный кабинет и выхода из него
    :param browser:
    """

    user_page = UserPage(browser.wd)
    user_login = UserLogin(browser.wd)
    breadcrumbs = BreadCrumbs(browser.wd)

    # Открывам главную страницу:
    browser.open_main_page()

    # Выбираем аккаунт
    user_page.my_account()

    # Нажимаем войти:
    user_page.log_in()

    # Очищаем поля и вводим данные для авторизации:
    user_login.fill_username(email)
    user_login.fill_password(password)
    user_login.login()

    # Собираем хлебные крошки после Login:
    account_breadcrumb = breadcrumbs.account_breadcrumb()

    # Нажимаем кнопку Logout для выхода из аккаунта:
    user_page.log_out()

    # Собираем хлебные крошки после Logout:
    logout_breadcrumb = breadcrumbs.logout_breadcrumb()

    # Подтвержаем выход из аккаунта:
    user_page.confirm_exit()

    # Проверяем хлебные крошки:
    assert account_breadcrumb == 'Account'
    assert logout_breadcrumb == 'Logout'


@pytest.mark.parametrize('currency', ["USD", "GBP", "EUR"])
def test_change_currency(browser, currency):
    """
    Проверка смены валюты в Header'е
    :param currency:
    :param browser:
    :return:
    """

    header = Header(browser.wd)

    # Открывам главную страницу:
    browser.open_main_page()

    # Выбираем parametrize.currency:
    header.change_currency(currency)

    # Проверяем, что была выбрана правильная валюта:
    new_currency = header.get_currency()
    assert currency == new_currency


def test_search_product(browser):
    """
    Проверка поиск товара на странице
    :param browser:
    """

    main_page = MainPage(browser.wd)
    search_page = SearchPage(browser.wd)

    # Открывам главную страницу:
    browser.open_main_page()

    # Очищаем поле ввода и вводим интересующий нас товар:
    main_page.search('Canon EOS 5D')
    search_query = search_page.get_search_query_text()
    search_product = search_page.get_search_product_text()

    # Проверяем, что был поиск по интересующему нас товару:
    assert search_query == 'Search - Canon EOS 5D'

    # Проверям, что в результатах поиска есть интересующий нас товар:
    assert search_product == 'Canon EOS 5D'


def test_add_to_cart(browser):
    """
    Проверка добавления товара в корзину
    :param browser:
    """
    search_page = SearchPage(browser.wd)
    product_page = ProductPage(browser.wd)

    # Открывам главную страницу:
    browser.open_main_page()

    # Ищем iPhone среди товаров на главной странице:
    search_page.click_product()

    # Вводим интересующее нас количество товара:
    product_page.quantity('2')

    # Нажимаем добавить в корзину:
    product_page.add_to_cart()

    # Проверяем, что товар был успешно добавлен:
    result = product_page.add_to_cart_result()
    assert 'Success' in result


def test_remove_from_cart(browser):
    """
    Проверка удаление товара из корзины
    :param browser:
    """

    product_page = ProductPage(browser.wd)

    # Добавляем товар в корзину:
    test_add_to_cart(browser)

    # Удаляем товар из корзины:
    product_page.delete_from_cart()

    # Проверяем, что товар был успешно удален:
    result = product_page.delete_from_cart_result()
    assert result == 'Your shopping cart is empty!'


@pytest.mark.parametrize('banner', ["iphone", "macbook"])
def test_next_banner(browser, banner):
    """
    Проверка переключения баннера
    :param browser:
    :param banner:
    :return:
    """
    main_page = MainPage(browser.wd)

    # Открываем главную страницу:
    browser.open_main_page()

    # Переключаем на следующий баннер:
    main_page.switch_next_banner()

    # Проверяем текущий баннер:
    main_page.check_banner_is_present(banner)

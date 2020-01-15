from locators.main_page import MainPage
from locators.header import Header
from locators.search_page import SearchPage
from locators.user_page import UserPage
from locators.breadcrumbs import BreadCrumbs
from locators.product_page import ProductPage
from page_objects.user_login import UserLogin
import yaml

conf = yaml.safe_load(open('configuration.yml'))

email = conf['user']['email']
password = conf['user']['password']


def test_login_user(browser):
    """
    Проверка авторизации пользователя в личный кабинет и выхода из него
    :param browser:
    """

    # Открывам главную страницу:
    browser.open_main_page()

    # Выбираем аккаунт и нажимаем войти:
    browser.wd.find_element(*UserPage.my_account).click()
    browser.wd.find_element(*UserPage.log_in).click()

    # Очищаем поля и вводим данные для авторизации:
    user_login = UserLogin(browser.wd)

    user_login.fill_username(email)
    user_login.fill_password(password)
    user_login.login()

    # Собираем хлебные крошки после Login:
    account_breadcrumb = browser.wd.find_element(
        *BreadCrumbs.account_breadcrumb
    ).text

    # Нажимаем кнопку Logout для выхода из аккаунта:
    browser.wd.find_element(*UserPage.log_out).click()

    # Собираем хлебные крошки после Logout:
    logout_breadcrumb = browser.wd.find_element(
        *BreadCrumbs.logout_breadcrumb
    ).text

    # Подтвержаем выход из аккаунта:
    browser.wd.find_element(*UserPage.continue_button).click()

    # Проверяем хлебные крошки:
    assert logout_breadcrumb == 'Logout'
    assert account_breadcrumb == 'Account'


def test_change_currency(browser):
    """
    Проверка смены валют в Header'е
    :param browser:
    """

    # Открывам главную страницу:
    browser.open_main_page()

    # Нажимаем на кнопку смены валюты и выбираем dollar:
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_dollar).click()
    dollar = browser.wd.find_element(*Header.current_currency).text

    # Нажимаем на кнопку смены валюты и выбираем pounds:
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_pound).click()
    pounds = browser.wd.find_element(*Header.current_currency).text

    # Нажимаем на кнопку смены валюты и выбираем euro:
    browser.wd.find_element(*Header.currency_button).click()
    browser.wd.find_element(*Header.currency_euro).click()
    euro = browser.wd.find_element(*Header.current_currency).text

    # Проверяем, что была выбрана правильная валюта:
    assert dollar == '$' and pounds == '£' and euro == '€'


def test_search_product(browser):
    """
    Проверка поиск товара на странице
    :param browser:
    """

    # Открывам главную страницу:
    browser.open_main_page()

    # Очищаем поле ввода и вводим интересующий нас товар:
    browser.wd.find_element(*MainPage.search_string).clear()
    browser.wd.find_element(*MainPage.search_string).send_keys('Canon EOS 5D')
    browser.wd.find_element(*MainPage.search_button).click()

    search_query = browser.wd.find_element(*SearchPage.search_query).text
    search_product = browser.wd.find_element(*SearchPage.Canon_EOS_5D).text

    # Проверяем, что был поиск по интересующему нас товару:
    assert search_query == 'Search - Canon EOS 5D'

    # Проверям, что в результатах поиска есть интересующий нас товар:
    assert search_product == 'Canon EOS 5D'


def test_add_to_cart(browser):
    """
    Проверка добавления товара в корзину
    :param browser:
    """

    # Открывам главную страницу:
    browser.open_main_page()

    # Ищем iPhone среди товаров на главной странице:
    browser.wd.find_element(*SearchPage.iPhone).click()

    # Ощищаем поле ввода и вводим интересующее нас количество товара:
    browser.wd.find_element(*ProductPage.quantity).clear()
    browser.wd.find_element(*ProductPage.quantity).send_keys("2")

    # Нажимаем добавить в корзину:
    browser.wd.find_element(*ProductPage.add_to_cart).click()

    # Проверяем, что товар был успешно добавлен:
    add_result = browser.wd.find_element(*ProductPage.alert_success).text
    assert 'Success' in add_result


def test_remove_from_cart(browser):
    """
    Проверка удаление товара из корзины
    :param browser:
    """

    # Добавляем товар в корзину:
    test_add_to_cart(browser)

    # Удаляем товар из корзины:
    browser.wd.find_element(*ProductPage.cart_button).click()
    browser.wd.find_element(*ProductPage.remove_product).click()
    browser.wd.find_element(*ProductPage.cart_button).click()

    # Проверяем, что товар был успешно удален:
    remove_result = browser.wd.find_element(*ProductPage.empty_cart).text
    assert remove_result == 'Your shopping cart is empty!'

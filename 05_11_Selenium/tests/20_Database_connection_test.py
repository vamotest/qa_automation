from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage
import yaml

conf = yaml.safe_load(open('configuration.yml'))

email = conf['admin']['email']
password = conf['admin']['password']


def test_database(database, browser):
    """
    Проверка работы, добавления и удаления данных БД с помощью Selenium
    :param database:
    :param browser:
    :return:
    """
    # Добавляем валюту в базу:
    database.add_currency()

    admin_login = AdminLogin(browser.wd)
    admin_page = AdminPage(browser.wd)

    # Открывам страницу администратора:
    browser.open_admin_page()

    # Очищаем поля и username вводим данные для авторизации:
    admin_login.fill_username(email)

    # Очищаем поля и password вводим данные для авторизации:
    admin_login.fill_password(password)

    # Нажимаем кнопку Login для входа в аккаунт:
    admin_login.login_button()

    # Получаем список валют на странице:
    titles = admin_page.get_currencies_titles()

    # Удаляем валюту из базы:
    database.delete_currency()

    # Проверяем, что добавленная валюта есть на странице:
    assert 'Russia Ruble' in titles

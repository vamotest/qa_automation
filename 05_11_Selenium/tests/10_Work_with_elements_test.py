from page_objects.admin_login import AdminLogin
from page_objects.admin_page import AdminPage

import yaml

conf = yaml.safe_load(open('configuration.yml'))

email = conf['admin']['email']
password = conf['admin']['password']

product_name = conf['new']['product_name']
meta_tag_title = conf['new']['meta_tag_title']
model = conf['new']['model']
price = conf['new']['price']
min_quantity = conf['new']['min_quantity']


def admin_authorization(browser):
    """
    Авторизация под учетной записью администратора
    :param browser:
    """

    admin_login = AdminLogin(browser.wd)

    # Открывам страницу администратора:
    browser.open_admin_page()

    # Очищаем поля и username вводим данные для авторизации:
    admin_login.fill_username(email)

    # Очищаем поля и password вводим данные для авторизации:
    admin_login.fill_password(password)

    # Нажимаем кнопку Login для входа в аккаунт:
    admin_login.login_button()


def open_products_from_catalog(browser):
    """
    Navigation -> Catalog -> Products
    :param browser:
    """

    admin_page = AdminPage(browser.wd)

    # В разделе Navigation выбираем Catalog:
    admin_page.click_catalog()

    # В разделе Catalog выбираем Products:
    admin_page.click_products()


def add_product(browser):
    """
    Добавление продукта
    :param browser:
    """

    admin_page = AdminPage(browser.wd)

    # Ищем поле "Product name", очищаем и вводим данные:
    admin_page.fill_product_name(product_name)

    # Ищем поле "Meta tag title", очищаем и вводим данные:
    admin_page.fill_meta_tag_title(meta_tag_title)

    # В навигационное панеле ищем "Data" и нажимаем:
    admin_page.click_navigation_data()

    # Ищем поле "Model", очищаем и вводим данные:
    admin_page.fill_model(model)

    # Ищем поле "Price", очищаем и вводим данные:
    admin_page.fill_price(price)

    # Ищем поле "Minimum Quantity", очищаем и вводим данные:
    admin_page.fill_min_quantity(min_quantity)


def test_add_new_product(browser):
    """
    Добавление нового продукта в Product List
    :param browser:
    """

    admin_page = AdminPage(browser.wd)

    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Navigation -> Catalog -> Products:
    open_products_from_catalog(browser)

    # Ищем кнопку "Add new" и нажимаем на нее:
    admin_page.add_new_button()

    # Добавляем продукт:
    add_product(browser)

    # Ищем кнопку "Save" и нажимаем на нее:
    admin_page.save_button()

    # Проверяем успешность добавления нового продукта в Product List:
    alert_success = admin_page.alert_success()

    # Проверяем успешность добавления нового продукта в Product List:
    assert 'Success: You have modified products!' in alert_success


def test_edit_product(browser):
    """
    Изменение продукта в Product List
    :param browser:
    """

    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Navigation -> Catalog -> Products:
    open_products_from_catalog(browser)

    # Выбираем продукт для измения и нажимаем на него:
    product_for_edit = browser.wd.find_elements(
        *AdminPage.Products.ProductList.product_for_edit)[1]
    product_for_edit.click()

    # Ищем кнопку "Edit" и нажимаем на нее:
    edit_button = browser.wd.find_elements(
        *AdminPage.Products.ProductList.edit_button)[0]
    edit_button.click()

    # Вводим данные нового продукта:
    add_product(browser)

    # Ищем кнопку "Save" и нажимаем на нее:
    save_button = browser.wd.find_element(*AdminPage.Products.AddProduct.save)
    save_button.click()

    # Проверяем успешность изменения продукта в Product List:
    alert_success = browser.wd.find_element(
        *AdminPage.Products.AddProduct.alert_success)
    assert 'Success: You have modified products!' in alert_success.text


def test_delete_product(browser):
    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Navigation -> Catalog -> Products:
    open_products_from_catalog(browser)

    product_for_delete = browser.wd.find_elements(
        *AdminPage.Products.ProductList.product_for_edit)[1]
    product_for_delete.click()

    # Ищем кнопку "Delete" и нажимаем на нее:
    delete_button = browser.wd.find_element(*AdminPage.Products.delete_button)
    delete_button.click()

    # Подтверждаем действие удаления на странице браузера:
    browser.accept_alert()

    # Проверяем успешность удаления продукта из Product List:
    alert_success = browser.wd.find_element(
        *AdminPage.Products.AddProduct.alert_success)
    assert 'Success: You have modified products!' in alert_success.text

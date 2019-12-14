from tests.07_Work_with_elements import admin_authorization,\
    open_products_from_catalog, add_product
from locators.admin_page import AdminPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import yaml

conf = yaml.safe_load(open('configuration.yml'))

product_name = conf['new']['product_name']
meta_tag_title = conf['new']['meta_tag_title']
model = conf['new']['model']
price = conf['new']['price']
min_quantity = conf['new']['min_quantity']


def wait_dashboard_title(browser):
    """
    Ожидаем появления заголовка "Dashboard" в течении 5 секунд:
    :param browser:
    """
    WebDriverWait(browser.wd, 5).until(EC.title_is('Dashboard'))


def test_add_new_product(browser):
    """
    Добавление нового продукта в Product List
    :param browser:
    """

    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Ожидаем появления заголовка "Dashboard" в течении 5 секунд:
    wait_dashboard_title(browser)

    # Navigation -> Catalog -> Products:
    open_products_from_catalog(browser)

    # Ожидаем появления кнопки "Add new" в течении 5 секунд и нажимаем на нее:
    add_new_button = WebDriverWait(browser.wd, 5).until(
        EC.element_to_be_clickable(*AdminPage.Products.add_new))
    add_new_button.click()

    # Добавляем продукт:
    add_product(browser)

    # Ожидаем появления кнопки "Save" в течении 5 секунд и нажимаем на нее:
    save_button = WebDriverWait(browser.wd, 5).until(
        EC.element_to_be_clickable(*AdminPage.Products.AddProduct.save))
    save_button.click()

    # Проверяем успешность добавления нового продукта в Product List:
    alert_success = browser.wd.find_element(
        *AdminPage.Products.AddProduct.alert_success)
    assert 'Success: You have modified products!' in alert_success.text


def test_edit_product(browser):
    """
    Изменение продукта в Product List
    :param browser:
    """

    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Ожидаем появления заголовка 'Dashboard' в течении 5 секунд:
    wait_dashboard_title(browser)

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

    # Ожидаем появления кнопки "Save" и нажимаем на нее:
    save_button = WebDriverWait(browser.wd, 5).until(
        EC.element_to_be_clickable(*AdminPage.Products.AddProduct.save))
    save_button.click()

    # Проверяем успешность изменения продукта в Product List:
    alert_success = browser.wd.find_element(
        *AdminPage.Products.AddProduct.alert_success)
    assert 'Success: You have modified products!' in alert_success.text


def test_delete_product(browser):
    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Ожидаем появления заголовка "Dashboard" в течении 5 секунд:
    wait_dashboard_title(browser)

    # Navigation -> Catalog -> Products:
    open_products_from_catalog(browser)

    # Выбираем продукт для измения и нажимаем на него:
    product_for_delete = browser.wd.find_elements(
        *AdminPage.Products.ProductList.product_for_edit)[1]
    product_for_delete.click()

    # Ожидаем появления кнопки "Delete" в течении 5 секунд и нажимаем на нее:
    delete_button = WebDriverWait(browser.wd, 5).until(
        EC.element_to_be_clickable(*AdminPage.Products.delete_button))
    delete_button.click()

    # Подтверждаем действие удаления на странице браузера:
    browser.accept_alert()

    # Проверяем успешность удаления продукта из Product List:
    alert_success = browser.wd.find_element(
        *AdminPage.Products.AddProduct.alert_success)
    assert 'Success: You have modified products!' in alert_success.text

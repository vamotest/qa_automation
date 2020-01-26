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
    admin_authorization(browser)
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

    # Ищем поле "Product name", очищаем и вводим данные:
    product_name_field = browser.wd.find_element(
        *AdminPage.Products.AddProduct.product_name)
    product_name_field.clear()
    product_name_field.send_keys(product_name)

    # Ищем поле "Meta tag title", очищаем и вводим данные:
    meta_tag_title_field = browser.wd.find_element(
        *AdminPage.Products.AddProduct.meta_tag_title)
    meta_tag_title_field.clear()
    meta_tag_title_field.send_keys(meta_tag_title)

    # В навигационное панеле ищем "Data" и нажимаем:
    navigation_data = browser.wd.find_element(
        *AdminPage.Products.AddProduct.navigation_data)
    navigation_data.click()

    # Ищем поле "Model", очищаем и вводим данные:
    model_field = browser.wd.find_element(
        *AdminPage.Products.AddProduct.model)
    model_field.clear()
    model_field.send_keys(model)

    # Ищем поле "Price", очищаем и вводим данные:
    price_field = browser.wd.find_element(
        *AdminPage.Products.AddProduct.price)
    price_field.clear()
    price_field.send_keys(price)

    # Ищем поле "Minimum Quantity", очищаем и вводим данные:
    min_quantity_field = browser.wd.find_element(
        *AdminPage.Products.AddProduct.min_quantity)
    min_quantity_field.clear()
    min_quantity_field.send_keys(min_quantity)


def test_add_new_product(browser):
    """
    Добавление нового продукта в Product List
    :param browser:
    """

    # Авторизация под учетной записью администратора:
    admin_authorization(browser)

    # Navigation -> Catalog -> Products:
    open_products_from_catalog(browser)

    # Ищем кнопку "Add new" и нажимаем на нее:
    add_new_button = browser.wd.find_element(*AdminPage.Products.add_new)
    add_new_button.click()

    # Добавляем продукт:
    add_product(browser)

    # Ищем кнопку "Save" и нажимаем на нее:
    save_button = browser.wd.find_element(*AdminPage.Products.AddProduct.save)
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

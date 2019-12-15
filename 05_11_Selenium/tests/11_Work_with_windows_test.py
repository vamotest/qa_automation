from locators.admin_login import AdminLogin
from locators.admin_page import AdminPage

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

import yaml


conf = yaml.safe_load(open('configuration.yml'))

email = conf['admin']['email']
password = conf['admin']['password']
path_to_file = conf['admin']['path_to_file']
filename = conf['admin']['filename']


def admin_authorization(browser):
    """
    Авторизация под учетной записью администратора
    :param browser:
    """

    # Открывам страницу администратора:
    browser.open_admin_page()

    # Очищаем поля и username вводим данные для авторизации:
    username_field = browser.wd.find_element(*AdminLogin.username)
    username_field.clear()
    username_field.send_keys(email)

    # Очищаем поля и password вводим данные для авторизации:
    password_field = browser.wd.find_element(*AdminLogin.password)
    password_field.clear()
    password_field.send_keys(password)

    # Нажимаем кнопку Login для входа в аккаунт:
    login_button = browser.wd.find_element(*AdminLogin.login_button)
    login_button.click()


def test_upload(browser):
    """
    Тест загрузки файла в панеле администратора
    """

    # Авторизация под учетной записью администратора
    admin_authorization(browser)

    # В разделе Navigation выбираем Catalog:
    catalog = browser.wd.find_element(*AdminPage.Navigation.catalog)
    catalog.click()

    # В разделе Catalog выбираем Downloads:
    downloads = browser.wd.find_element(
        *AdminPage.Navigation.CatalogMenu.downloads)
    downloads.click()

    # Нажимаем кнопку "Add New"
    add_new_button = browser.wd.find_element(
        *AdminPage.Products.add_new)
    add_new_button.click()

    # Нажимаем кнопку "Upload"
    upload_button = browser.wd.find_element(
        *AdminPage.Products.AddProduct.upload_button)
    upload_button.click()

    # Вводим путь до файл загрузки:
    upload_file = browser.wd.find_element(
        *AdminPage.Products.AddProduct.upload_file)
    upload_file.send_keys(path_to_file)

    actions = ActionChains(browser.wd)
    actions.pause(0.5).perform()

    # Нажимаем кнопку "OK" на ответ "Your file was successfully uploaded!":
    Alert(browser.wd).accept()

    # Ищем поле "Download Name", очищаем и вводим имя файла:
    download_name = browser.wd.find_element(
        *AdminPage.Products.AddProduct.download_name)
    download_name.clear()
    download_name.send_keys(filename)

    # Ищем кнопку "Save" и нажимаем на нее
    save_button = browser.wd.find_element(*AdminPage.Products.AddProduct.save)
    save_button.click()

    # Записываем знание о статусе загрузки:
    alert_upload_success = browser.wd.find_element(
        *AdminPage.Products.AddProduct.alert_upload_success)

    # Закрываем браузер:
    browser.quit()

    # Проверяем успешность загрузки файла:
    assert 'Success: You have modified products!' in alert_upload_success.text

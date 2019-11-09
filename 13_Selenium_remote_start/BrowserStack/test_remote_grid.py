from webdriver_info import remote_driver
import time


def test_remote_grid():
    # Получаем информацию о remote driver:
    driver = remote_driver()

    # Максимизируем окно браузера:
    driver.maximize_window()

    # Переходим по ссылке:
    driver.get("http://www.google.com")

    # Проверяем есть ли имя поисковой система Google в заголовке:
    if "Google" not in driver.title:
        raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")

    # Вводим запрос игры в поисковую стороку:
    elem.send_keys("Flip a coin")

    # Отправляем запрос:
    elem.submit()

    # Выводим имя заголовка:
    print(driver.title)

    # Ожидаем выполнения игры:
    time.sleep(5)

    # Закрываем окно браузера:
    driver.quit()


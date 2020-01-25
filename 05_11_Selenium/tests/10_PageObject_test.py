from page_objects.main_page import MainPage
import pytest


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

def test_start_driver(browser):
    """
    Проверяем, что в выбранном или дефолтном браузере открывается
    запрашиваемая или дефолтная страница и находится заголовок 'Your Store'
    :param
    browser = default or user browser
    """
    browser.open_main_page()
    title = browser.wd.title
    browser.quit()

    assert title == 'Your Store'

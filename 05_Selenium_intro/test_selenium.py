
def test_start_driver(chosen_driver, opencart_url):
    """
    Проверяем, что в выбранном или дефолтном браузере открывается
    запрашиваемая или дефолтная страница и находится заголовок 'Your Store'
    :param
    chosen_driver = default or user browser,
    opencart_url = default or user url
    """
    chosen_driver.get(opencart_url)
    assert chosen_driver.title == 'Your Store'
    chosen_driver.close()

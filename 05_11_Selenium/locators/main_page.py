from selenium.webdriver.common.by import By


class MainPage:

    # Лого:
    logo = (By.CSS_SELECTOR, '#logo')

    # Поисковая строка и кнопка:
    search_string = (By.CSS_SELECTOR, '[class="form-control input-lg"]')
    search_button = (By.CSS_SELECTOR, '[class="btn btn-default btn-lg"]')



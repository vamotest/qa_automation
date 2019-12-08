from selenium.webdriver.common.by import By


class Header:

    # Валюты:
    currency_button = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
    current_currency = (By.CSS_SELECTOR, "strong")
    currency_euro = (By.CSS_SELECTOR, '#form-currency [name="EUR"]')
    currency_pound = (By.CSS_SELECTOR, '#form-currency [name="GBP"]')
    currency_dollar = (By.CSS_SELECTOR, '#form-currency [name="USD"]')


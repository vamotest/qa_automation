from selenium.webdriver.common.by import By


class BreadCrumbs:

    account_breadcrumb = (By.CSS_SELECTOR, '#account-account > ul li:nth-child(2)')
    logout_breadcrumb = (By.CSS_SELECTOR, '.breadcrumb li:nth-child(3)')

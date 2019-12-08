from selenium.webdriver.common.by import By


class SearchPage:

    search_query = (By.CSS_SELECTOR, '#content h1')

    Canon_EOS_5D = (By.LINK_TEXT, 'Canon EOS 5D')
    iPhone = (By.LINK_TEXT, 'iPhone')

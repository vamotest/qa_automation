from locators.search_page import SearchPage as search_page


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def get_search_query_text(self):
        search_query = self.driver.find_element(*search_page.search_query)
        return search_query.text

    def get_search_product_text(self):
        search_product = self.driver.find_element(*search_page.Canon_EOS_5D)
        return search_product.text

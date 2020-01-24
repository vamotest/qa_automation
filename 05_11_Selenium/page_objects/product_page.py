from locators.product_page import ProductPage as product_page


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def quantity(self, text):

        quantity = self.driver.find_element(*product_page.quantity)
        quantity.clear()
        quantity.send_keys(text)

    def add_to_cart(self):
        add_to_cart = self.driver.find_element(*product_page.add_to_cart)
        add_to_cart.click()

    def add_to_cart_result(self):
        result = self.driver.find_element(*product_page.alert_success)
        return result.text

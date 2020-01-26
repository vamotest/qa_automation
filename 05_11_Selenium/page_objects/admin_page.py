from locators.admin_page import AdminPage as admin_page


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def click_catalog(self):
        catalog = self.driver.find_element(*admin_page.Navigation.catalog)
        catalog.click()

    def click_products(self):
        products = self.driver.find_element(
            *admin_page.Navigation.CatalogMenu.products)
        products.click()

    def logout(self):
        button = self.driver.find_element(*admin_page.logout)
        button.click()

    def fill_product_name(self, product_name):
        field = self.driver.find_element(
            *admin_page.Products.AddProduct.product_name)
        field.clear()
        field.send_keys(product_name)

    def fill_meta_tag_title(self, meta_tag_title):
        field = self.driver.find_element(
            *admin_page.Products.AddProduct.meta_tag_title)
        field.clear()
        field.send_keys(meta_tag_title)

    def click_navigation_data(self):
        navigation_data = self.driver.find_element(
            *admin_page.Products.AddProduct.navigation_data)
        navigation_data.click()

    def fill_model(self, model):
        field = self.driver.find_element(*admin_page.Products.AddProduct.model)
        field.clear()
        field.send_keys(model)

    def fill_price(self, price):
        field = self.driver.find_element(*admin_page.Products.AddProduct.price)
        field.clear()
        field.send_keys(price)

    def fill_min_quantity(self, min_quantity):
        field = self.driver.find_element(
            *admin_page.Products.AddProduct.min_quantity)
        field.clear()
        field.send_keys(min_quantity)

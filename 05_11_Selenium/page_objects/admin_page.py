from locators.admin_page import AdminPage as admin_page


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def alert_success(self):
        alert = self.driver.find_element(
            *admin_page.Products.AddProduct.alert_success)
        return alert.text

    def logout(self):
        button = self.driver.find_element(*admin_page.logout)
        button.click()

    # Navigation:

    def click_catalog(self):
        catalog = self.driver.find_element(*admin_page.Navigation.catalog)
        catalog.click()

    def click_products(self):
        products = self.driver.find_element(
            *admin_page.Navigation.CatalogMenu.products)
        products.click()

    def click_navigation_data(self):
        navigation_data = self.driver.find_element(
            *admin_page.Products.AddProduct.navigation_data)
        navigation_data.click()

    # Fields:

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

    # Buttons:

    def add_new_button(self):
        button = self.driver.find_element(*admin_page.Products.add_new)
        button.click()

    def save_button(self):
        button = self.driver.find_element(*admin_page.Products.AddProduct.save)
        button.click()

    def delete_button(self):
        button = self.driver.find_element(*admin_page.Products.delete_button)
        button.click()

    # Actions with the product:

    def product_for_edit(self):
        product = self.driver.find_elements(
            *admin_page.Products.ProductList.product_for_edit)[1]
        product.click()

    def product_for_delete(self):
        product = self.driver.find_elements(
            *admin_page.Products.ProductList.product_for_edit)[1]
        product.click()

    def edit_button(self):
        button = self.driver.find_elements(
            *admin_page.Products.ProductList.edit_button)[0]
        button.click()

    # Titles:

    def get_currencies_titles(self):
        system = self.driver.find_element(*admin_page.Navigation.system)
        system.click()

        localisation = self.driver.find_element(
            *admin_page.Navigation.SystemMenu.localisation)
        localisation.click()

        currencies = self.driver.find_element(
            *admin_page.Navigation.SystemMenu.LocalizationMenu.currencies)
        currencies.click()

        currencies_titles = self.driver.find_elements(
            *admin_page.Currencies.currency_title)

        titles = []

        for currency in currencies_titles:
            titles.append(currency.text)
        return titles

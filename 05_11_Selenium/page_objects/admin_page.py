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

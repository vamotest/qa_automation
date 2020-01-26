from locators.breadcrumbs import BreadCrumbs as breadcrumbs


class BreadCrumbs:

    def __init__(self, driver):
        self.driver = driver

    def account_breadcrumb(self):
        breadcrumb = self.driver.find_element(*breadcrumbs.account)
        return breadcrumb.text

    def logout_breadcrumb(self):
        breadcrumb = self.driver.find_element(*breadcrumbs.logout)
        return breadcrumb.text

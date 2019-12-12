from selenium.webdriver.common.by import By


class AdminPage:

    class Navigation:

        catalog = (By.CSS_SELECTOR, '#menu-catalog a')

        class CatalogMenu:

            products = (By.XPATH, '//*[@id="menu-catalog"]//*[text() = "Products"]')

    class Products:

        add_new = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
        delete_button = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
        success_delete = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

        class ProductList:

            edit_button = (By.CSS_SELECTOR, '#form-product .table-responsive tr [data-original-title="Edit"]')
            product_for_edit = (By.CSS_SELECTOR,'#form-product .table-responsive tr input[type="checkbox"]')

        class AddProduct:

            navigation_data = (By.XPATH, '//*[text() = "Data"]')

            product_name = (By.CSS_SELECTOR, '#input-name1')

            meta_tag_title = (By.CSS_SELECTOR, '#input-meta-title1')
            model = (By.CSS_SELECTOR, '#input-model')
            price = (By.CSS_SELECTOR, '#input-price')
            min_quantity = (By.CSS_SELECTOR, '#input-quantity')

            save = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')
            alert_success = (By.CLASS_NAME, 'alert-success')

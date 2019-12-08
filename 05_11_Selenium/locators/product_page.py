from selenium.webdriver.common.by import By


class ProductPage:

    add_to_wish_list = (By.CSS_SELECTOR, "//button[@data-original-title='Add to Wish List']")
    alert_success = (By.CLASS_NAME, "alert-success")
    quantity = (By.CSS_SELECTOR, '#input-quantity')
    add_to_cart = (By.CSS_SELECTOR, '#button-cart')
    remove_product = (By.CSS_SELECTOR, '[class="btn btn-danger btn-xs"]')
    cart_button = (By.CSS_SELECTOR, '[class="btn btn-inverse btn-block btn-lg dropdown-toggle"]')
    empty_cart = (By.CSS_SELECTOR, '[class="dropdown-menu pull-right"]')

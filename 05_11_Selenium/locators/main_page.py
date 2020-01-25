from selenium.webdriver.common.by import By


class MainPage:

    # Лого:
    logo = (By.CSS_SELECTOR, '#logo')

    # Поисковая строка и кнопка:
    search_string = (By.CSS_SELECTOR, '[class="form-control input-lg"]')
    search_button = (By.CSS_SELECTOR, '[class="btn btn-default btn-lg"]')

    # Banner elements:
    next_banner = (By.XPATH, "//div[@id='slideshow0']/parent::div//div[@class='swiper-button-next']")
    previous_banner = (By.XPATH, "//div[@id='slideshow0']/parent::div//div[@class='swiper-button-prev']")

    iphone_banner = (By.CSS_SELECTOR, "img[alt='iPhone 6']")
    macbook_banner = (By.CSS_SELECTOR, "img[alt='MacBookAir']")
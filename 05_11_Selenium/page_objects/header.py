from locators.header import Header as header


class Header:

    def __init__(self, driver):
        self.driver = driver

    def change_currency(self, currency):

        currency_button = self.driver.find_element(*header.currency_button)
        currency_button.click()

        if currency == 'USD':
            usd_button = self.driver.find_element(*header.currency_usd)
            usd_button.click()
        elif currency == 'GBP':
            gbp_button = self.driver.find_element(*header.currency_gbp)
            gbp_button.click()
        elif currency == 'EUR':
            eur_button = self.driver.find_element(*header.currency_eur)
            eur_button.click()

    def get_currency(self):
        currency = self.driver.find_element(*header.current_currency)
        if currency.text == '€':
            return 'EUR'
        elif currency.text == '$':
            return 'USD'
        elif currency.text == '£':
            return 'GBP'

from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import ItemPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_the_button(*ItemPageLocators.BASKET_BUTTON)

    def book_in_basket(self):
        item = self.browser.find_element(*ItemPageLocators.BOOK_NAME)
        item_in_basket = self.browser.find_element(*ItemPageLocators.BOOK_IN_BASKET_NAME)
        assert item.text == item_in_basket.text, "Item not in the basket"
        print(f"{item_in_basket.text} in the basket")

    def correct_price_in_basket(self):
        price = self.browser.find_element(*ItemPageLocators.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*ItemPageLocators.BASKET_PRICE)
        assert price.text == price_in_basket.text, "Price incorrect in the basket"
        print(f"Price {price_in_basket.text} is correct")


from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_the_button(*ProductPageLocators.BASKET_BUTTON)

    def book_in_basket(self):
        item = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        item_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET_NAME)
        assert item.text == item_in_basket.text, "Item not in the basket"
        print(f"{item_in_basket.text} in the basket")

    def correct_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price.text == price_in_basket.text, "Price incorrect in the basket"
        print(f"Price {price_in_basket.text} is correct")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"




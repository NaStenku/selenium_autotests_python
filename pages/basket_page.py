from selenium_autotests_python.pages.base_page import BasePage
from selenium_autotests_python.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Register form is not presented"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators. BASKET_WITH_ITEMS), "Basket is not empty"

    def go_to_basket(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        login_link.click()


from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")


class ItemPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                     "p:nth-child(1) > strong")
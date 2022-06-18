from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_WITH_ITEMS = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs "
                                    "> span > a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                     "p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


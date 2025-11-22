from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    MESSAGE_NAME_OF_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    NAME_OF_ITEM = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    MESSAGE_ABOUT_COST_OF_CART = (By.CSS_SELECTOR,"#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div ")
    COST_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    COST_OF_ITEM = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
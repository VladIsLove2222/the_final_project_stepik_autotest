from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "There is some items in the basket"

    def should_be_text_about_emptyness(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IN_EMPTY_BASKET), "There is no text about emptyness of the basket"


    
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_CART)
        button.click()

    def should_be_correct_messages(self):
        self.should_be_message_about_add_to_cart()
        self.should_be_correct_item_in_message()
        self.should_be_message_about_cost()
        self.should_be_cost_equal()

    def should_be_message_about_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART), "Message about adding to the cart is not found"

    def should_be_correct_item_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_OF_ITEM).text == self.browser.find_element(*ProductPageLocators.NAME_OF_ITEM).text, "The name of item in message is not correct"

    def should_be_message_about_cost(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_COST_OF_CART), "Message about cost of your cart is not present"

    def should_be_cost_equal(self):
        assert self.browser.find_element(*ProductPageLocators.COST_IN_MESSAGE).text == self.browser.find_element(*ProductPageLocators.COST_OF_ITEM).text, "Cost in your cart isn't equal to cost of item" 
        
  




        


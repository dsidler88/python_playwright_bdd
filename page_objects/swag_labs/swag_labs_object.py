from page_objects.base_page import BasePage
from page_objects.swag_labs.swag_labs_locators import SwagLabsLocators
from utils.faker_helper import get_faker_uuid, fake_str


class SwagLabs(BasePage):
    def open_swaglabs(self):
        self.go_to_url(SwagLabsLocators.ADDRESS)
    
    def login_swaglabs(self, username, password):
        self.page.type(SwagLabsLocators.USERNAME_FIELD, username)
        self.page.type(SwagLabsLocators.PASSWORD_FIELD, password)
        self.page.click(SwagLabsLocators.LOGIN_BUTTON)

    def open_backpack(self):
        self.click(SwagLabsLocators.BACKPACK)

    def add_item_to_cart(self):
        self.click(SwagLabsLocators.ADD_TO_CART)


    def visit_shopping_cart(self):
        self.click(SwagLabsLocators.SHOPPING_CART_ICON)

    def validate_item_was_added(self, item_name):
        cart_items = self.page.query_selector_all(SwagLabsLocators.CART_ITEMS)
        for item in cart_items:
            name_element = item.query_selector(SwagLabsLocators.ITEM_NAME)
            if name_element and item_name in name_element.inner_text():
                return True
        return False
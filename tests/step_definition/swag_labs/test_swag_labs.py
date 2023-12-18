"""As a user, I can add items to my shopping cart feature tests."""

from pytest_bdd import (
    parsers,
    given,
    scenario,
    then,
    when,
)
from page_objects.swag_labs.swag_labs_object import SwagLabs

@scenario('swag_labs.feature', 'I can use the UI to add different items to my cart')
def test_i_can_use_the_ui_to_add_different_items_to_my_cart(page):
    """I can use the UI to add different items to my cart."""
    #swag_labs = SwagLabs(page)

#pytest-bdd automatically matches the decorators to the correct scenario
@given('I have navigated to the correct URL and logged in')
def navigate_to_swaglabs(page):
    """I have navigated to the correct URL and logged in."""
    SwagLabs(page).open_swaglabs()
    # #if page.get_by_placeholder("someone@example.com").is_visible():
    # page.get_by_placeholder("someone@example.com").click()
    # page.get_by_placeholder("someone@example.com").fill("")
    # page.get_by_placeholder("someone@example.com").press("Enter")
    # page.locator("#i0118").fill("")
    # page.locator("#idSIButton9").click()
    #else:
    print("ms login skipped")
    SwagLabs(page).login_swaglabs("standard_user", "secret_sauce")


@when('I click "Add To Cart"')
def add_to_cart(page):
    """I click "Add To Cart"."""
    SwagLabs(page).add_item_to_cart()


#NEED parsers.parse for parameterized tests, and they are ONLY for Scenario Outline, not Scenario (in feature file)
@when(parsers.parse('I click on "{Item}"'))
def click_on_item(page, Item):
    """I click on "<Item>"."""
    SwagLabs(page).open_backpack()


@when('I navigate to the shopping cart')
def navigate_to_shopping_cart(page):
    """I navigate to the shopping cart."""
    SwagLabs(page).visit_shopping_cart()


@then(parsers.parse('"{Item}" should be in my list of items'))
def validate_item_in_list(page, Item):
    """"<Item>" should be in my list of items."""
    SwagLabs(page).validate_item_was_added(Item)


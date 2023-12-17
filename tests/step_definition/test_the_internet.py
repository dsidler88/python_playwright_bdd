"""As a user i can browse the heroku internet page feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from page_objects.the_internet.the_internet_page_object import TheInternetPage


@scenario('the_internet.feature', 'I can experiment with different controls')
def test_i_can_experiment_with_different_controls():
    """I can experiment with different controls."""


@given('I have navigated to the correct URL')
def _(page):
    """I have navigated to the correct URL."""
    ##id
    ##TheInternetPage(page).


@when('I click checkbox 1')
def _():
    """I click checkbox 1."""
    pass


@when('I click on the "Checkboxes" link')
def _():
    """I click on the "Checkboxes" link."""
    pass


@then('checkbox 1 should be active')
def _():
    """checkbox 1 should be active."""
    pass


@then('checkbox 2 should also be active')
def _():
    """checkbox 2 should also be active."""
    pass
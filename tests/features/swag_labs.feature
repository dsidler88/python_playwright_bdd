@hotlink
Feature: As a user, I can add items to my shopping cart

  Background: 
    Given I have navigated to the correct URL and logged in

  Scenario Outline: I can use the UI to add different items to my cart
    When I click on "<Item>"
    And I click "Add To Cart"
    And I navigate to the shopping cart
    Then "<Item>" should be in my list of items

  Examples:
    | Item               |
    | Sauce Labs Backpack|
    | Sauce Labs Bike Light|
    | Sauce Labs Bolt T-Shirt|

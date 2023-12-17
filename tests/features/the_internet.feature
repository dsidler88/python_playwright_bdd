@hotlink
Feature: As a user i can browse the heroku internet page

  Background: 
    Given I have navigated to the correct URL

  Scenario Outline: I can experiment with different controls
    When I click on the "Checkboxes" link
    When I click checkbox 1
    Then checkbox 1 should be active
    And checkbox 2 should also be active
@hotlink @login
  Feature: As a user,I want to login with username and password,In order to access the application.

    Background:
      Given I open the url

    Scenario: I wants to login with username and password
      When I input username and password
      Then I should see the login page


    Scenario: I want to open the login page,So that I can login to my account.
      Then I can see the I in login page.
Feature: Test the functionality of the Register Page

    Background: I am on the Register Page
    Given I am on the Register Page

    Scenario: Check that trying to register without completing any field displays error fields
      When I click on the Register button
      Then First name error is displayed
      Then Last name error is displayed
      Then Email error is displayed
      Then Password error is displayed
      Then Confirm password error is displayed
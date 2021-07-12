Feature: Forgot Sign-on Password for Mongolian Customer

  Background: Common Steps
    Given I launch the Khan Bank application
    When I click on Forgot Password link

  Scenario: Verifying if Forgot Password Page for Mongolian Customer is displayed
    And I select the login password to be reset
    Then I should be displayed with the Forgot password page for Mongolian Customer
    And I close the browser

  Scenario: Validation of warning message when no password type is selected
    And I click on Continue button without selecting a password
    Then Warning message should be displayed
    And I close the browser





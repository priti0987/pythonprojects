Feature:Valid  SignUp_Page_Firefox

Scenario: To Check Valid Data For Signup Khan Bank Retail Envirnoment In English Language in Firefox
    Given I launch the Khan Bank Retail application in Firefox
     When I Click on Language Link
      And I Click on SignUp link in Firefox
      And I Enter all Valid Values in signup page
     Then I enter OTP Values
      And I Click on Back Button
      And I close the browser

Feature:SignUp

  Scenario: To check Signup For Khan Bank Retail Application In Firefox For English language
    Given I launch the Khan Bank Retail application in Firefox
     When Click On Language Link
      And Open SignUpPage
      And Set Valid Drop Down Values
      And Enter Input fields For signUp
     Then I close the browser

Feature:SignUp

  Scenario: To check InValid Signup For Khan Bank Retail Application In Firefox For English language
    Given I launch the Khan Bank Retail application in Firefox
     When Click On Language Link
      And Open SignUpPage
      And Set Valid dropdown Values
      And Enter Input fields For signUp
     Then I close the browser


    Scenario: To check Valid Signup For Khan Bank Retail Application In Firefox For English language
    Given I launch the Khan Bank Retail application in Firefox
     When Click On Language Link
      And Open SignUpPage
      And Set Valid Values
     Then I close the browser


      Scenario: To Check Valid signup for khan bank corporate application in Firefor for Mongolian Language
    Given I launch the Khan Bank Corporate application in Firefox
    When Open SignUpPage
     And Set Valid Values
    Then I close the browser

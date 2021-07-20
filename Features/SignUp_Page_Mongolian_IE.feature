Feature:SignUp_Page_Mongolian_IE

  Scenario: To Check Valid Data For Signup Khan Bank Retail Envirnoment In Mongolian Language

    Given I launch the Khan Bank Retail application in IE
     When Click On Language Link
      And Open SignUpPage In IE
      And Set Valid dropdown Values for IE
      And Set ValidSignUpdata
     Then I close the browser

   Scenario:To Check InValid Data For Signup Khan Bank Retail Envirnoment in Mongolian Language
    Given I launch the Khan Bank Retail application in IE
     When Click On Language Link
      And Open SignUpPage In IE
      And Set Valid dropdown Values for IE
      And Set ValidSignUpdata
     Then I close the browser



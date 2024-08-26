Feature: Smoke Functionality
  @TC01 @smoke
  Scenario: TC01 login/logout functionality with valid credentials
    Given The user navigates to login page
    When The user enters a valid username and password
    And the user clicks on the Login button
    Then the user navigates to the home page
    When the users clicks on logout button
    Then the user navigates to login page

 @TC02 @smoke
 Scenario: TC02 login functionality with invalid credentials
   Given The user navigates to login page
   When the user enters an invalid username and password
   And the user clicks on the Login button
   Then the user should see error message

  @TC03 @smoke
  Scenario: TC03 login functionality with out credentials
    Given The user navigates to login page
    When the user enters empty username and password
    And the user clicks on the Login button
    Then the user should see required field validation message

 @TC04 @smoke
 Scenario:TC04 login page layout
   Given The user navigates to login page
   Then the user should see login panel layout

 @TC05 @smoke
 Scenario: TC05 OTP layout
   Given The user navigates to login page
   When the user clicks on the forget password
   Then the user navigate to the OTP panel
   And the user verify the OTP panel layout
   When the user enter the username in OTP panel
   Then the request OTP button should enable

 @TC06 @smoke
 Scenario: TC06 Change password panel layout
   Given The user navigates to login page
   When The user enters a valid username and password
   And the user clicks on the Login button
   Then the user navigates to the home page
   When the users clicks on change password button
   When the user clicks on cancel button
   Then the user navigates to the home page
   When the users clicks on logout button
   Then the user navigates to login page

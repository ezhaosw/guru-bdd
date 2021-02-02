Feature: Customer checks account number, account type and balance
  As a customer,
  I want to check my account number, account type and balance using a valid
  user ID and password

Background:
  Given I am on the home page
  When I type "32468" in the userid field
  And I type "johnpwd1" in the password field
  And I press the "login" button
  Then I will see the "customer" page

Scenario: Check Balance
  Given I am on the "customer" page
  When I click the "Balance Enquiry" link
  And I see the "Balance Enquiry Form" page
  And I select "88047" from the drop-down menu
  And I press the "submit" button
  Then I will see the "Balance Details" page

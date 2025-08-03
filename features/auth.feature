@auth @smoke
Feature: Authentication Module
  As a user, I want to login with valid credentials so that I can access the application

  Scenario: TC_AUTH_01 - Login with Valid credentials
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

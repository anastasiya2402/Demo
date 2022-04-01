# Created by anastasiashabanskaya at 3/7/22
Feature: Regression of MyUT Web Portal functionalities

  Background: Login to MyUT Web Portal
    Given Navigate to "myut"
#   Given Navigate to "context.url"
    And wait for the page to load
    And Click on button Login by text in header
    Then Enter ashaban into UserName
    And Enter Casper_060210 into Password
    Then Click on button Sign in by text
    And wait for the page to load


  Scenario: Verification of MyUT Web Portal page
    Given Verify that Welcome Anastasia Shabanskaya is present
    And Page title should be "myUT"
    Then Verify that following buttons/links/texts are displayed
      | Field                              | Element_type               |
      | Account Maintenance                | login-elements-in-header   |
      | Parent/Guest Payment               | login-elements-in-header   |
      | Welcome Anastasia Shabanskaya      | login-elements-in-header   |
      | Logout                             | login-elements-in-header   |
      | NEW INTL STUDENT                   | body-data-elements         |
      | STUDENT                            | body-data-elements         |
      | STUDENT RESOURCES                  | body-data-elements         |
      | GRADUATE                           | body-data-elements         |
      | INTERNATIONAL                      | body-data-elements         |
      | INACTIVE EMPLOYEE                  | body-data-elements         |
      | COVID-19 UPDATES                   | body-data-elements         |
      | UT COMMUNITY                       | body-data-elements         |
      | LIBRARY                            | body-data-elements         |
      | UTMC                               | body-data-elements         |
      | UNIVERSITY DIRECTORY               | body-data-elements         |


  Scenario: Rockets Email - Logging in with Valid Credentials - Happy Path
   Given Choose tab "Student"
   Then Switch to iframe and go to Rockets Email
   And wait for the page to load
   And If Stay signed in? is asked, then click button "No" by value
   Then Verify that SA appears in the upper right corner
   And Page title should be "Mail - Shabanskaya, Anastasia - Outlook"

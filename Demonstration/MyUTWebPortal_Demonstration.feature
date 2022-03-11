# Created by anastasiashabanskaya at 3/7/22
Feature: Regression of MyUT Web Portal functionalities

  Background: Login to MyUT Web Portal
    Given Navigate to "myut"
    And wait for the page to load


  Scenario: Login with Valid credentials - Happy Path
    Given Click on button Login by text in header
    Then Enter ashaban into UserName
    And Enter Casper_060210 into Password
    Then Click on button Sign in by text
    And wait for the page to load
    And Verify that Welcome Anastasia Shabanskaya is present
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

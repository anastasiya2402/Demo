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

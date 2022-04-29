# Created by anastasiashabanskaya at 3/7/22
Feature: Regression of MyUT Web Portal functionalities

  Background: Login to MyUT Web Portal
    Given Navigate to "myut"
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
      | STUDENT                            | body-data-elements         |
      | STUDENT RESOURCES                  | body-data-elements         |
      | GRADUATE                           | body-data-elements         |
      | INACTIVE EMPLOYEE                  | body-data-elements         |
      | COVID-19 UPDATES                   | body-data-elements         |
      | UT COMMUNITY                       | body-data-elements         |
      | LIBRARY                            | body-data-elements         |
      | UTMC                               | body-data-elements         |
      | UNIVERSITY DIRECTORY               | body-data-elements         |


  Scenario: Rockets Email - Logging in with Valid Credentials - Happy Path
   Given Choose tab "Student"
   Then Switch to iframe and go to a new window for Rockets Email
   And wait for the page to load
   And If Stay signed in? is asked, then click button "No" by value
   Then Verify that SA appears in the upper right corner
   And Page title should be "Mail - Shabanskaya, Anastasia - Outlook"

  Scenario: Technology Services & Software Information - College of Natural Sciences and Mathematics page Verification
   Given Choose tab "Student"
   Then Switch to iframe and go to a new window for Natural Sciences and Mathematics
   And wait for the page to load
   Then Verifying table 1 data on the page by comparing two dictionaries
      | Description            | Specifications                                                                           |
      | Processor              | Intel Core i5 or i7 (Intel i5 processors are preferred)                                  |
      | Memory                 | 8GB RAM or more (8GB is preferred)                                                       |
      | Hard Drive             | 256 GB or more (256 GB or higher SSD drives are preferred)                               |
      |Wireless Card (laptops) | Wireless cards 802.11 ac or ax (Intel cards are preferred)                               |
      | Operating System       | Windows 10, or Mac OS 10.12 or higher                                                    |
      | Software Packages      | Microsoft Office 365, Office 2019, Microsoft Office for Mac 365, or 2019, and Open Office|
      | Anti-virus Software    |Microsoft Windows Defender, (already installed with Windows 10) McAfee, Norton, or AVG    |
      | Web Browsers           | Chrome, Firefox, Edge, Internet Explorer (PC only) or Safari (Apple only)                |
      |Anti-Spyware/Anti-Adware| Malwarebytes or Super Anti-Spyware                                                       |
      | Other Programs         | Adobe Reader and VLC Media Player                                                        |
      | Warranty               | 3 years or more                                                                          |
      | Accessories            | Flash Drive, Jump Drive 8 GB or higher, cable lock, laptop carrying bag, network cable   |


  @no_background
  Scenario: Department of Mathematics and Statistics - Verifying that buttons in header are displayed/enabled
    Given Open "https://www.utoledo.edu/nsm/mathstats/"
    And wait for the page to load
    And Verify that button Visit is enabled
    And Verify that button Visit is displayed
    And Verify that button Apply is enabled
    And Verify that button Apply is displayed
    And Verify that button Give is enabled
    And Verify that button Give is displayed
    And Verify that button Search is enabled
    And Verify that button Search is displayed
    And Verify that button Menu is enabled
    Then Verify that button Menu is displayed


 Scenario: Technology Support - Student Software page Verification - HTML Table - 1st and 2nd, 1st and 3rd rows
   Given Choose tab "Student"
   Then Switch to iframe and go to a new window for Student Software
   And wait for the page to load
   And Verifying table 0 data by comparing two vertical dictionaries consisting of rows 1 and 2
      |ADOBE                       |OFFICE 365                   |ENTERPRISE                     |THIRD PARTY                 |
      |Https:\\Software.Utoledo.Edu|Https:\\Office365.Utoledo.Edu|Https:\\Myutaccount.Utoledo.Edu|Https:\\Utoledo.Onthehub.Com|
   Then Verifying table 0 data by comparing two vertical dictionaries consisting of rows 1 and 3
      |ADOBE             |OFFICE 365 |ENTERPRISE     |THIRD PARTY     |
      |Adobe Acrobat ($) |Excel      |AntiVirus Info |Windows 10 ($)  |
   And Verifying table 0 data by comparing two vertical dictionaries consisting of rows 1 and 4
      |ADOBE                    |OFFICE 365 |ENTERPRISE            |THIRD PARTY      |
      |Adobe Creative Suite ($) |One Drive  |Eduroam Wireless Info |Mind Manager ($) |
   Then Verifying table 0 data by comparing two vertical dictionaries consisting of rows 1 and 5
      |ADOBE |OFFICE 365 |ENTERPRISE |THIRD PARTY    |
      |      |Outlook    |EndNote    |Norton 360 ($) |


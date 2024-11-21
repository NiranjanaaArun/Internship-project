# Created by Admin at 11/7/2024
Feature: Reely Main page

  Scenario: User can open the off plan page and go through the pagination
    Given Open the sign-in page
    When Log in to the page
    #When Click on off plan option at the left side menu
    #Then Verify the right page opens
    Then Go to the final page using the pagination button
    Then Go back to the first page using the pagination button

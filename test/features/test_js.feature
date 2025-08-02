@reuse_driver
Feature: CI Juice Shop
  Actions Before the Feature: 
    Given I open the Juice Shop

  Scenario: Create User Juice Shop
    Given I create user on Juice Shop

  Scenario: Login into Juice Shop
    Given I login into Juice Shop

  Scenario: Search and add product
    Given I search for "Apple Juice"
    Given I add item to cart

  Scenario: Send Customer Feedback
    Given I go to customer feedback page
    When I fill customer feedback form


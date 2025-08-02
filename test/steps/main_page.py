import time

from behave import when, step

from pageobjects.login import LoginPageObject
from pageobjects.main_page import MainPagePageObject


@step('I go to customer feedback page')
def step_impl(context):
    MainPagePageObject().side_menu.click()
    MainPagePageObject().customer_feedback.click()
    

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    MainPagePageObject().home.click()
    MainPagePageObject().search_button.click()
    MainPagePageObject().search.text = search_term

@step('I add item to cart')
def step_impl(context):
    MainPagePageObject().add_to_cart.click()
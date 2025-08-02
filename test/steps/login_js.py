import time

from behave import step

from pageobjects.login import LoginPageObject

@step('I open the Juice Shop')
def step_impl(context):
    
    LoginPageObject().open()
    time.sleep(1)  # Wait for the login to complete

@step('I login into Juice Shop')
def step_impl(context):
    
    LoginPageObject().login()
    time.sleep(1)  # Wait for the login to complete

@step('I create user on Juice Shop')
def step_impl(context):
    
    LoginPageObject().create_user()
    time.sleep(1)  # Wait for the login to complete



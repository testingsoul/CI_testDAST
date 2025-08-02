import time

from behave import step

from pageobjects.customer_feedback import CustomerFeedbackPageObject


@step('I fill customer feedback form')
def step_impl(context):
    CustomerFeedbackPageObject().comment.text = "This is a test feedback comment."
    CustomerFeedbackPageObject().set_rating(5) # Assuming clicking the button sets the rating
    CustomerFeedbackPageObject().captcha_eval()
    CustomerFeedbackPageObject().submit.click()
    


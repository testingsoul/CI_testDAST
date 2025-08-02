import time
from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button, Select


class LoginPageObject(PageObject):
    def init_page_elements(self):
        self.account_menu = Button(By.ID, "navbarAccount")
        self.login_link = Button(By.ID, "navbarLoginButton")
        self.username = InputText(By.ID, "email")
        self.password = InputText(By.ID, "password")
        self.submit = Button(By.ID, "loginButton")
        self.close_welcome_banner = Button(By.XPATH, "//button[@aria-label='Close Welcome Banner']")
        self.cookie_consent = Button(By.XPATH, "//a[@aria-label='dismiss cookie message']")

        self.new_customer = Button(By.XPATH, "//div[@id='newCustomerLink']/a")
        self.new_username = InputText(By.ID, "emailControl")
        self.new_password = InputText(By.ID, "passwordControl")
        self.rep_password = InputText(By.ID, "repeatPasswordControl")
        self.security_question = Button(By.ID, "mat-select-1")
        self.security_question_sel = Button(By.ID, "mat-option-3")
        self.security_answer = InputText(By.ID, "securityAnswerControl")
        self.register = Button(By.ID, "registerButton")


    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        try: 
            self.close_welcome_banner.click()
            self.cookie_consent.click()
        except Exception as e:
            print(f"Error closing welcome banner or cookie consent: {e}")
        return self


    def login(self):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.account_menu.click()
        self.login_link.click()
        self.wait_until_loaded()
        user = {
            'username': self.config.get('Test', 'username'),
            'password': self.config.get('Test', 'password')
        }
        self.username.text = user['username']
        self.password.text = user['password']
        self.submit.click()

    def create_user(self):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.account_menu.click()
        self.login_link.click()
        

        self.wait_until_loaded()
        time.sleep(2)
        self.new_customer.click()
        user = {
            'username': self.config.get('Test', 'username'),
            'password': self.config.get('Test', 'password')
        }
        self.new_username.text = user['username']
        self.new_password.text = user['password']
        self.rep_password.text = user['password']
        self.security_question.click()
        self.security_question_sel.click()
        self.security_answer.text = "Any answer"
        self.register.click()

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.username.wait_until_visible()
        return self


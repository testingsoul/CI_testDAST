from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button


class MainPagePageObject(PageObject):
    def init_page_elements(self):
        self.close_welcome_banner = Button(By.XPATH, "//button[@aria-label='Close Welcome Banner']")
        self.cookie_consent = Button(By.XPATH, "//a[@aria-label='dismiss cookie message']")
        self.side_menu = Button(By.XPATH, "//button[@aria-label='Open Sidenav']")
        self.customer_feedback = Button(By.XPATH, "//a[@aria-label='Go to contact us page']")
        self.search_button = Button(By.ID, "searchQuery")
        self.search = InputText(By.ID, "mat-input-1")
        self.home = Button(By.ID, "homeButton")
        self.add_to_cart = Button(By.XPATH, "//div[@class='basket-btn-container']/button")

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        self.close_welcome_banner.click()
        self.cookie_consent.click()
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


    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.username.wait_until_visible()
        return self
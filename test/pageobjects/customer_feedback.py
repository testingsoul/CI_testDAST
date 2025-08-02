from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button, Text


class CustomerFeedbackPageObject(PageObject):
    def init_page_elements(self):
        self.comment = InputText(By.XPATH, "//textarea[@aria-label='Field for entering the comment or the feedback']")
        self.rating = Button(By.XPATH, "//div[@style='transform: translateX(26.5px);']")
        self.captcha_to_eval = Text(By.ID, "captcha")
        self.captcha = InputText(By.ID, "captchaControl")
        self.submit = Button(By.ID, "submitButton")


    def captcha_eval(self):
        captcha_text = self.captcha_to_eval.text
        result = eval(captcha_text)
        self.captcha.text = str(result)
        return self

    def set_rating(self, value):
        """Set the mat-slider to the desired value."""
        slider = self.driver.find_element(By.XPATH, "//input[@matsliderthumb]")
        min_value = int(slider.get_attribute("min"))
        max_value = int(slider.get_attribute("max"))
        width = slider.size['width']

        # Calculate the offset
        offset = int((value - min_value) / (max_value - min_value) * width)
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.comment.wait_until_visible()
        return self


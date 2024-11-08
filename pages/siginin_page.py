from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SigninPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    SIGN_IN = (By.CSS_SELECTOR, "a[href='#'][class*='login-button']")

    def open_signin_page(self):
        self.open('https://soft.reelly.io')
        sleep(6)

    def valid_credentials(self):
        self.input_text('niranjanaa.anand@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Watsup123!', *self.PASSWORD_FIELD)
        sleep(5)
        self.click(*self.SIGN_IN)
        sleep(6)


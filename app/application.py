from pages.base_page import Page
from pages.main_page import MainPage
from pages.siginin_page import SigninPage

class Application:

    def __init__(self,driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.siginin_page = SigninPage(driver)

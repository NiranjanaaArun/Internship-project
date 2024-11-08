from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep

class MainPage(Page):

    OFFPLAN= (By.CSS_SELECTOR, 'address.menu-twobutton')
    OFFPLAN_TITLE= (By.CSS_SELECTOR, "[class*='page-title off_plan']")
    NEXT_PAGE = (By.CSS_SELECTOR, "a[wized='nextPageProperties']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "a[wized='properties-pagination']")
    CURRENT_PAGE = (By.CSS_SELECTOR, "div[wized='currentPageProperties']")
    TOTAL_PAGES = (By.CSS_SELECTOR, "div[wized='totalPageProperties']")

    def headers(self):
        self.click(*self.OFFPLAN)
        sleep(10)

    def verify_title(self):
        self.wait_until_appears(*self.OFFPLAN_TITLE)
        self.scroll()
        sleep(2)

    def next_page(self):
        while True:
            try:
                current_page_number = self.find_element(*self.CURRENT_PAGE)
                total_page_number = self.find_element(*self.TOTAL_PAGES)
                if current_page_number == total_page_number:
                    print("Reached the last page.")
                    break
                self.find_element(*self.NEXT_PAGE).click()
                sleep(2)
            except(NoSuchElementException, StaleElementReferenceException):
                print("Next button not found or stale. Assuming last page reached.")
                break

    def prev_page(self):
        while True:
            try:
                current_page_number = self.find_element(*self.CURRENT_PAGE)
                if current_page_number == 1:
                    print("Reached first page")
                    break
            except(NoSuchElementException, StaleElementReferenceException):
                print("Next button not found")
                break




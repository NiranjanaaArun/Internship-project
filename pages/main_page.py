from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep

class MainPage(Page):

    OFFPLAN= (By.CSS_SELECTOR, "[class='menu-twobutton']")
    OFFPLAN_TITLE= (By.CSS_SELECTOR, "[class*='page-title off_plan']")
    NEXT_PAGE = (By.CSS_SELECTOR, "a[wized='nextPageProperties']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "div[wized='previousPageProperties']")
    CURRENT_PAGE = (By.CSS_SELECTOR, "div[wized='currentPageProperties']")
    TOTAL_PAGES = (By.CSS_SELECTOR, "div[wized='totalPageProperties']")

    def headers(self):
        self.click(*self.OFFPLAN)
        sleep(10)

    def verify_title(self):
        self.wait_until_appears(*self.OFFPLAN_TITLE)
        #self.driver.find_element("targetElement").scrollIntoView();
        sleep(2)

    def next_page(self):
        self.scroll()
        while True:
                current_page_element = self.find_element(*self.CURRENT_PAGE)
                total_page_element = self.find_element(*self.TOTAL_PAGES)

                current_page_number = int(current_page_element.text)
                total_page_number = int(total_page_element.text)

                if current_page_number >= total_page_number:
                    print("Reached the last page.")
                    break
                self.wait_to_be_clickable_click(*self.NEXT_PAGE)
                sleep(2)


    def prev_page(self):
        while True:
                current_page_number = int(self.find_element(*self.CURRENT_PAGE).text)
                if current_page_number == 1:
                    print("Reached first page")
                    break
                self.scroll()
                self.find_element(*self.PREVIOUS_PAGE).click()
                sleep(2)


from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when ('Click on {option} at the left side menu')
def sign_in_page(context, option):
    print(f"Option selected: {option}")
    context.app.main_page.headers()

@then ('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.main_page.verify_title()

@then ('Go to the final page using the pagination button')
def final_page(context):
    context.app.main_page.next_page()
    # while True:
    #     try:
    #         next_button = context.driver.find_element(*NEXT_PAGE)
    #         next_button.click()
    #         sleep(5)
    #     except NoSuchElementException:
    #         break
@then ('Go back to the first page using the pagination button')
def previous_page(context):
    context.app.main_page.prev_page()
    # while True:
    #     try:
    #         next_button = context.driver.find_element(*PREVIOUS_PAGE)
    #         next_button.click()
    #         sleep(5)
    #     except NoSuchElementException:
    #         break
    #
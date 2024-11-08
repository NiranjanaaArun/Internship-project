from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given ('Open the sign-in page')
def sign_in_page(context):
    context.app.siginin_page.open_signin_page()

@when ('Log in to the page')
def login(context):
    context.app.siginin_page.valid_credentials()
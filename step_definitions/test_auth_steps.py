from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from pages.login_page import LoginPage

scenarios('../features/auth.feature')

@given('user is on Login Page')
def user_on_login_page(page, config, request):
    login_page = LoginPage(page)
    login_page.goto(config['login_page_base_url'])
    request.login_page = login_page

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def enter_credentials(request, username, password, config):
    request.login_page.login(username, password)

@when('click Login Button')
def click_login():
    # Already handled in login method
    pass

@then(parsers.parse('verify page has text "{text}"'))
def verify_products(request, text, config):
    assert request.login_page.is_products_visible(), f'Expected text {text} not found on page.'

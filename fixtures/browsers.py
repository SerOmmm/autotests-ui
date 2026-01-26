import os
import pytest
from playwright.sync_api import Page, BrowserContext, Browser


@pytest.fixture(scope='session')
def chromium_browser(playwright: pytest.fixture) -> Browser:
    return playwright.chromium.launch(headless=False)

@pytest.fixture(scope='session')
def chromium_context(chromium_browser: Browser) -> BrowserContext:
    return chromium_browser.new_context()

@pytest.fixture(scope='session')
def chromium_page(chromium_context) -> Page:
    return chromium_context.new_page()

@pytest.fixture(scope='session')
def initialize_browser_state(chromium_context, chromium_page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    chromium_context.storage_state(path='browser-state.json')


@pytest.fixture(scope='function')
def chromium_page_with_state(chromium_browser, initialize_browser_state):
    context = chromium_browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    page.close()
    context.close()
    if os.path.exists("browser-state.json"):
        os.remove("browser-state.json")




# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         yield browser.new_page()
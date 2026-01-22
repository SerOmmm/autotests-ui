import pytest
from playwright.sync_api import Page, BrowserContext, Browser

@pytest.fixture
def chromium_context(browser: Browser) -> BrowserContext:
    return browser.new_context()

@pytest.fixture
def chromium_page(chromium_context: BrowserContext) -> Page:
    return chromium_context.new_page()


# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         yield browser.new_page()
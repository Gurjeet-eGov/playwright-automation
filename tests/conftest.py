# shared fixtures
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

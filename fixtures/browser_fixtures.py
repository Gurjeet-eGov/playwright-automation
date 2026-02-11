import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_chr():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# @pytest.fixture(scope="session")
# def browser_chr(playwright, browser_type_launch_args):
#     launch_args = dict(browser_type_launch_args)
#     launch_args.setdefault("headless", False)
#     browser = playwright.chromium.launch(**launch_args)
#     yield browser
#     browser.close()

@pytest.fixture(scope="session")
def page_chr(browser_chr):
    context = browser_chr.new_context()
    page = context.new_page()
    yield page
    context.close()
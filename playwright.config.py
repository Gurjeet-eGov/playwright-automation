# Playwright specific config

from playwright.sync_api import BrowserType

def pytest_playwright_browser_args(browser_name):
    return {
        "headless": True,
        "slow_mo": 0
    }

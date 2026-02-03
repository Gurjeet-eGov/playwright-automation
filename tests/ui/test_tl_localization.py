import pytest

import pytest
from utils.localization_scanner import find_non_localized_text

BASE_URL = "https://digit-ui-url"  # move to env later

TL_WORKFLOW_PAGES = [
    "/citizen/tl/apply",
    "/citizen/tl/details",
    "/employee/tl/search",
]

SUPPORTED_LOCALES = ["en-IN", "hi-IN"]

@pytest.mark.ui
@pytest.mark.localization
@pytest.mark.parametrize("page", SUPPORTED_LOCALES, indirect=True)
def test_trade_license_ui_localization(page, request):
    locale = request.param

    failures = {}

    for path in TL_WORKFLOW_PAGES:
        url = f"{BASE_URL}{path}"
        page.goto(url, wait_until="networkidle")

        # Expand all dropdowns to expose hidden options
        dropdowns = page.locator("select")
        for i in range(dropdowns.count()):
            dropdowns.nth(i).click()

        visible_text = page.evaluate("() => document.body.innerText")

        non_localized = find_non_localized_text(visible_text)

        if non_localized:
            failures[url] = non_localized
            page.screenshot(
                path=f"screenshots/{locale}_{path.replace('/', '_')}.png"
            )

    if failures:
        error_message = f"\nLocalization failures for locale [{locale}]:\n"
        for url, keys in failures.items():
            error_message += f"\nPage: {url}\nKeys: {sorted(keys)}\n"

        pytest.fail(error_message)

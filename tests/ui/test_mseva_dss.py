
import re, time, pytest
from utils import helpers

MODULE = "DSS"
BASE_URL = helpers.get_env("host")
MSEVA_DSS_URL = "/dashboard/"

@pytest.mark.ui
def test_sure_dashboard(page_chr):

    page = page_chr
    page.goto(BASE_URL + MSEVA_DSS_URL)

    # Wait for navigation to employee landing page
    page.wait_for_load_state("networkidle")

    # Extract page text
    dss_body = page.locator("#divToPrint")
    page.wait_for_load_state("networkidle")
    dss_body.wait_for(state="visible", timeout=15000)
    locales = dss_body.inner_text()
    locales = re.split(r'[\n\t]+', locales)
    locales = [item.strip() for item in locales if item.strip()]

    # Find localization leaks
    loc_codes = helpers.find_loc_codes(locales)
    helpers.write_json(loc_codes, MODULE + '_locales.json')
    assert True

@pytest.mark.ui
def test_pt_dashboard(page_chr):

    page = page_chr
    page.goto(BASE_URL + MSEVA_DSS_URL)

    # Wait for navigation to employee landing page
    page.wait_for_load_state("networkidle")

    # Extract page text
    dss_body = page.locator("#divToPrint")
    page.wait_for_load_state("networkidle")
    dss_body.wait_for(state="visible", timeout=15000)

    pt_card = page.locator(".MuiTypography-root").filter(has_text="Property Tax")
    pt_card.click()
    page.wait_for_load_state("networkidle")

    dss_body = page.locator("#divToPrint")
    table_row = dss_body.get_by_role("row").first
    table_row.wait_for(state="visible", timeout=10000)

    locales = dss_body.inner_text()
    locales = re.split(r'[\n\t]+', locales)
    locales = [item.strip() for item in locales if item.strip()]
    print(locales)
    # Find localization leaks
    loc_codes = helpers.find_loc_codes(locales)
    helpers.write_json(loc_codes, 'PT_locales.json')
    time.sleep(2)
    assert True


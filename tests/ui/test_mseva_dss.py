
import re, time, pytest
from utils import helpers
from playwright.sync_api import expect

BASE_URL = helpers.get_env("host")
MSEVA_DSS_URL = "/dashboard/"

@pytest.mark.ui
@pytest.mark.localization
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
    locales = locales.replace('\t', '\n')
    # Find localization leaks
    loc_codes = helpers.find_loc_codes(locales)
    helpers.write_json(loc_codes, 'test_sure_dashboard.json')
    expect(dss_body).to_be_visible()

@pytest.mark.ui
@pytest.mark.localization
def test_pt_dashboard_rev(page_chr):
    page = page_chr
    page.goto(BASE_URL + MSEVA_DSS_URL)

    # Wait for navigation to employee landing page
    page.wait_for_load_state("networkidle")

    # Extract page text
    dss_body = page.locator("#divToPrint")
    dss_body.wait_for(state="visible", timeout=15000)

    pt_card = page.locator(".MuiTypography-root").filter(has_text="Property Tax")
    expect(pt_card).to_be_visible()
    pt_card.click()
    page.wait_for_load_state("networkidle")

    dss_body = page.locator("#divToPrint")
    table_row = dss_body.get_by_role("row").first
    table_row.wait_for(state="visible", timeout=10000)
    locales = dss_body.inner_text()
    # Find localization leaks
    loc_codes = helpers.find_loc_codes(locales, isTable=True)
    helpers.write_json(loc_codes, 'test_pt_dashboard_rev.json')
    expect(table_row).to_be_visible()

@pytest.mark.ui
@pytest.mark.localization
def test_pt_dashboard_rev_tb(page_chr):
    page = page_chr
    page.goto(BASE_URL + MSEVA_DSS_URL)
    page.wait_for_load_state("networkidle")
    pt_card = page.locator(".MuiTypography-root").filter(has_text="Property Tax")
    pt_card.click()
    body = page.locator("#divToPrint")
    body.wait_for(state="visible", timeout=10000)
    table_data = helpers.get_table_data(body)
    table_data = re.split(r'[\t\n]', table_data)
    table_data = helpers.find_loc_codes(table_data)
    helpers.write_json(table_data, 'test_pt_dashboard_rev_tb.json')
    assert True

@pytest.mark.ui
@pytest.mark.localization
def test_tl_dashboard_rev(page_chr):

    page = page_chr
    page.goto(BASE_URL + MSEVA_DSS_URL)

    # Wait for navigation to employee landing page
    page.wait_for_load_state("networkidle")

    # Extract page text
    dss_body = page.locator("#divToPrint")
    dss_body.wait_for(state="visible", timeout=15000)

    tl_card = page.locator(".MuiTypography-root").filter(has_text="Trade License")
    expect(tl_card).to_be_visible()
    tl_card.click()
    page.wait_for_load_state("networkidle")

    dss_body = page.locator("#divToPrint")
    table_row = dss_body.get_by_role("row").first
    table_row.wait_for(state="visible", timeout=10000)
    locales = dss_body.inner_text()
    # Find localization leaks
    loc_codes = helpers.find_loc_codes(locales, isTable=True)
    helpers.write_json(loc_codes, 'test_tl_dashboard_rev.json')
    expect(table_row).to_be_visible()

@pytest.mark.ui
@pytest.mark.localization
def test_tl_dashboard_rev_tb(page_chr):
    page = page_chr
    page.goto(BASE_URL + MSEVA_DSS_URL)
    page.wait_for_load_state("networkidle")
    pt_card = page.locator(".MuiTypography-root").filter(has_text="Trade License")
    pt_card.click()
    body = page.locator("#divToPrint")
    body.wait_for(state="visible", timeout=10000)
    table_data = helpers.get_table_data(body)
    table_data = re.split(r'[\t\n]', table_data)
    table_data = helpers.find_loc_codes(table_data)
    helpers.write_json(table_data, 'test_tl_dashboard_rev_tb.json')
    assert True

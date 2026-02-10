import pytest, time, re

from playwright.sync_api import Page
from utils import helpers

def test_demo(page: Page):

    # Language selection
    # page = context.new_page()
    page.goto("https://unified-demo.digit.org/digit-ui/employee/user/language-selection")

    # Get all available languages
    language_dd = page.locator(".language-button-container button")
    language_dd.first.wait_for()
    languages = []
    for i in range(language_dd.count()):
        button_text = language_dd.nth(i).inner_text()
        languages.append(button_text)
    print("\nAvailable languages:", languages)
    
    # Language selection
    locale = languages[0]
    print("\nSelected languages:", locale)
    language_dd.get_by_text(locale).click()
    page.get_by_role("button").get_by_text("Continue").click()


    # Employee Login
    page.locator("input[name='username']").fill("TL_SU")
    page.locator("input[name='password']").fill("eGov@1234")

    # City selection
    dropdown_wrapper = page.locator(".employee-select-wrap.login-city-dd")
    dropdown_wrapper.click()
    options_box = page.locator("#jk-dropdown-unique")
    options_box.wait_for(state="visible", timeout=5000)
    options_box.locator(".profile-dropdown--item").nth(1).click()

    page.locator("button[type='submit']").click()

    # Wait for navigation to employee landing page
    page.wait_for_url("**/digit-ui/employee")

    # Extract page text
    body = page.locator("[id='root']")
    text = body.inner_text().split('\n')
    # Sidebar interaction
    sidebar = page.locator(".sidebar")
    sidebar.hover()
    # Sidebar click to expand (TL module)
    sidebar.locator("[data-for='jk-side-TRADE_LICENSE']").click()
    sidebar_text = sidebar.inner_text().split('\n')

    print("\nLogged in page text:", text, type(text))
    print("\nSidebar text:", sidebar_text, type(sidebar_text))

    body.locator(".employee-app-container").hover()
    page.get_by_role("link", name="Dashboard").click()
    dss_body = page.locator("#divToPrint")
    dss_body.wait_for(state="visible", timeout=15000)
    dss_text = dss_body.inner_text()
    dss_text = re.split(r'[\n\t]+', dss_text)
    dss_text = [item.strip() for item in dss_text if item.strip()]
    print("\nDSS text:", dss_text, type(dss_text))


    loc_list = helpers.list_cleanup(text + sidebar_text + dss_text)
    print("\nFinal:", loc_list)

    # Find localization leaks
    leaks = helpers.find_loc_codes(loc_list, 'resources/source.json')
    print("\nLocalization leaks:", leaks)
    helpers.write_csv(leaks, 'tl_locales.csv')
    helpers.write_json(leaks, 'tl_locales.json')

    time.sleep(3)
    assert True




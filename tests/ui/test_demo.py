import pytest, time

from playwright.sync_api import Page

def test_demo(context):
    page = context.new_page()
    page.goto("https://unified-demo.digit.org/digit-ui/employee/user/language-selection")

    language_buttons = page.locator(".language-button-container button")

    language_buttons.first.wait_for()
    languages = []
    for i in range(language_buttons.count()):
        button_text = language_buttons.nth(i).inner_text()
        languages.append(button_text)

    print("\nAvailable languages:", languages)
    locale = languages[0]
    print("\nSelected languages:", locale)
    language_buttons.get_by_text(locale).click()

    page.get_by_role("button").get_by_text("Continue").click()

    page.locator("input[name='username']").fill("TL_SU")
    page.locator("input[name='password']").fill("eGov@1234")


    dropdown_wrapper = page.locator(".employee-select-wrap.login-city-dd")
    dropdown_wrapper.click()
    options_box = page.locator("#jk-dropdown-unique")
    options_box.wait_for(state="visible", timeout=5000)
    options_box.locator(".profile-dropdown--item").nth(1).click()

    page.locator("button[type='submit']").click()

    page.wait_for_url("**/digit-ui/employee")

    body = page.locator("[id='root']")
    text = body.inner_text().split('\n')

    sidebar = page.locator(".sidebar")
    sidebar.hover()
    
    sidebar.locator("[data-for='jk-side-TRADE_LICENSE']").click()
    sidebar_text = sidebar.inner_text().split('\n')

    print("\nLogged in page text:", text, type(text))
    print("\nSidebar text:", sidebar_text, type(sidebar_text))

    text.extend(sidebar_text)
    print("\nFinal:", text)

    time.sleep(3)
    assert True




@pytest.mark.localization
def test_emp_login(page: Page):
    # page = context.new_page()
    page.goto("https://unified-demo.digit.org/digit-ui/employee/user/language-selection")

    language_buttons = page.locator(".language-button-container button")

    language_buttons.first.wait_for()
    languages = []
    for i in range(language_buttons.count()):
        button_text = language_buttons.nth(i).inner_text()
        languages.append(button_text)

    print("\nAvailable languages:", languages)
    locale = languages[1]
    print("\nSelected languages:", locale)
    language_buttons.get_by_text(locale).click()

    page.get_by_role("button").get_by_text("Continue").click()

    page.locator("input[name='username']").fill("TL_SU")
    page.locator("input[name='password']").fill("eGov@1234")


    dropdown_wrapper = page.locator(".employee-select-wrap.login-city-dd")
    dropdown_wrapper.click()
    options_box = page.locator("#jk-dropdown-unique")
    options_box.wait_for(state="visible", timeout=5000)
    options_box.locator(".profile-dropdown--item").nth(1).click()

    page.locator("button[type='submit']").click()



    time.sleep(5)
    assert True



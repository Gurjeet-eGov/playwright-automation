import pytest, time

from playwright.sync_api import Page

@pytest.mark.localization
def test_unitdemo(context):
    page = context.new_page()
    page.goto("https://unified-demo.digit.org/digit-ui/employee/user/language-selection")

    language_buttons = page.locator(".language-selector")
    buttons = language_buttons.locator("button")

    print(buttons.all_inner_texts())

    # page.get_by_role("button").get_by_text(buttons.all_inner_texts()[1]).click()
    time.sleep(2)
    assert True




# @pytest.mark.localization
# def test_unitdemo(context):
#     page = context.new_page()
#     page.goto("https://unified-demo.digit.org/digit-ui/employee/user/login")

#     page.locator("input[name='username']").fill("PGR_SU")
#     page.locator("input[name='password']").fill("eGov@123")


#     dropdown_wrapper = page.locator(".employee-select-wrap.login-city-dd")
#     dropdown_wrapper.click()
#     options_box = page.locator("#jk-dropdown-unique")
#     options_box.wait_for(state="visible", timeout=5000)
#     options_box.get_by_text("Victoria City").click()


#     page.locator("button[type='submit']").click()

#     time.sleep(5)
#     assert True



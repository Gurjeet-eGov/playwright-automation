import pytest

@pytest.fixture(scope="session")
def tl_context(browser_chr):
    ctx = browser_chr.new_context()
    page = ctx.new_page()
    page.goto("https://unified-demo.digit.org/digit-ui/employee/user/login")
    page.wait_for_load_state("domcontentloaded")
    page.locator("input[name='username']").wait_for(state="visible")

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
    page.wait_for_load_state("networkidle")
    
    yield ctx
    ctx.close()
    


import re, time, pytest
from utils import helpers

@pytest.mark.ui
def test_tl_dashboard(tl_context):

    page = tl_context.new_page()
    page.goto("https://unified-demo.digit.org/digit-ui/employee")

    # Wait for navigation to employee landing page
    page.wait_for_load_state("networkidle")

    # Extract page text
    page.get_by_role("link", name="Dashboard").click()
    dss_body = page.locator("#divToPrint")
    dss_body.wait_for(state="visible", timeout=15000)
    dss_text = dss_body.inner_text()
    print("\nRaw DSS Text:", dss_text, type(dss_text))
    dss_text = re.split(r'[\n\t]+', dss_text)
    dss_text = [item.strip() for item in dss_text if item.strip()]

    # loc_list = helpers.list_cleanup(dss_text)
    print("\nUI Text:", dss_text)

    # Find localization leaks
    leaks = helpers.find_loc_codes(dss_text)
    print("\nLocalization leaks:", leaks)
    helpers.write_csv(leaks, 'tl_locales.csv')
    helpers.write_json(leaks, 'tl_locales.json')

    time.sleep(3)
    assert True

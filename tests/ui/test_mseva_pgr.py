
import re, time, pytest
from utils import helpers
from playwright.sync_api import expect
from pages.Login import EmployeeLogin

BASE_URL = helpers.get_env("host")
LOGIN_URL = BASE_URL + "/employee/language-selection"
LOC_FILENAME = "TestMsevaPgr.json"

class TestMsevaPgr:

    USERNAME = helpers.get_creds("PGR").get("username")
    PASSWORD = helpers.get_creds("PGR").get("password")
    TENANT = helpers.get_creds("PGR").get("tenantId")
    loc_codes = []

    @pytest.fixture(scope="class", autouse=True)
    def pgr_fixture(self, browser_chr):
        ctx = browser_chr.new_context()
        page = ctx.new_page()
        page.goto(LOGIN_URL)
        page.wait_for_load_state("networkidle")

        employeeLogin = EmployeeLogin()
        employeeLogin.languageSelectionMonoUI(page, "English")
        # employeeLogin.login_continue_btn.click()

        # page.get_by_role("button").filter(has_text="English").click()
        # page.get_by_role("button").filter(has_text="Continue").click()


        page.wait_for_load_state("networkidle")
        # Employee Login
        page.locator("#employee-phone").fill(self.USERNAME)
        page.locator("#employee-password").fill(self.PASSWORD)
        page.get_by_role("textbox", name="City *").click()
        CityPicker = page.locator(".citipicker-dialog")
        CityPicker.wait_for(state="visible", timeout=5000)
        page.get_by_text("Testing").click()
        page.get_by_role("button").filter(has_text="Continue").click()

        # Wait for navigation to employee landing page
        page.wait_for_url("**/employee/inbox")
        page.wait_for_load_state("networkidle")
        page.close()
        yield ctx
        ctx.close()
        helpers.write_json(self.loc_codes, LOC_FILENAME)
  

    @pytest.mark.ui
    def test_pgr_emp(self, pgr_fixture):
        page = pgr_fixture.new_page()

        # Create Complaint UI
        page.goto(BASE_URL + '/employee/create-complaint')
        page.wait_for_load_state("networkidle")
        page_root = page.locator('[class=" col-xs-12"]')
        # page_text = page_root.inner_text()
        # self.loc_codes.extend(helpers.find_loc_codes(page_text))
        
        # Create Complaint form
        page_root.locator("#add-complaint").fill("Test Citizen Name")
        page_root.locator("#complainant-mobile-no").fill("9999999991")
        page_root.locator("#houseNo").fill("HN 123, ST 123")
        page_root.locator("#landmark").fill("TST LNDMRK")
        page.locator("[id='additional details']").fill("Test Additional Details")

        # Complaint type popup
        page.locator("[id='complaint-type']").click()
        page.locator("[id='complainttype-search']").fill("Dead Animals")
        page.locator("[data-localization='Dead Animals']").click()

        # City selection dropdown 
        city_field = page.locator("[id='city']")
        city_field.get_by_text("Select").click()
        city_field.get_by_role("textbox").fill("pb.testing")
        page.get_by_role("menuitem", name="pb.testing").click()

        # Locality selection dropdown 
        page.get_by_text("Choose Locality/Mohalla").click()
        page.get_by_role("menuitem", name="Azad Nagar - WARD-").click()

        # Submit complaint
        page.get_by_role("button").click()

        time.sleep(5)



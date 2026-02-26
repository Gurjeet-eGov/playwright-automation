
import re, time, pytest
from utils import helpers
from playwright.sync_api import expect
from pages.Login import EmployeeLogin
from pages.LandingPage import EmpMonoUI

BASE_URL = helpers.get_env("host")
LOC_FILENAME = "TestMsevaPgr.json"

class TestMsevaPgr:

    USERNAME = helpers.get_creds("PGR").get("username")
    PASSWORD = helpers.get_creds("PGR").get("password")
    TENANT = helpers.get_creds("PGR").get("tenantId")
    CITY = helpers.get_creds("PGR").get("city")
    LANGUAGE = "English"
    loc_codes = []

    @pytest.fixture(scope="class", autouse=True)
    def pgr_emp_ctx_fixture(self, browser_chr):

        # returns employee ui login context

        LOGIN_URL = BASE_URL + "/employee/language-selection"

        context = browser_chr.new_context()
        page = context.new_page()
        EmpLoginPom = EmployeeLogin(page)

        page.goto(LOGIN_URL)
        page.wait_for_load_state("networkidle")

        # Language-select page
        EmpLoginPom.select_language(self.LANGUAGE)
        page.wait_for_load_state("networkidle")

        # Employee Login
        EmpLoginPom.login_employee(username=self.USERNAME,
                                     password=self.PASSWORD,
                                     tenant_id=self.TENANT)

        # Wait for navigation to employee landing page
        page.wait_for_url("**/employee/inbox")
        page.wait_for_load_state("networkidle")
        page.close()
        yield context
        context.close()
        helpers.write_json(self.loc_codes, LOC_FILENAME)
  
    def test_pgr_empHomePageNav(self, pgr_emp_ctx_fixture):
        page = pgr_emp_ctx_fixture.new_page()
        page.goto(BASE_URL + "/employee")
        page.wait_for_load_state("networkidle")
        
        EmpPom = EmpMonoUI(page)

        EmpPom.left_menu_selection("PGR-1")
        EmpPom.left_menu_selection("CREATE-COMPLAINT-0")
        page.wait_for_load_state("networkidle")
        page.locator("#create-complaint-card").wait_for(state="visible")
        page.close()

    @pytest.mark.ui
    def test_pgr_createComplaint(self, pgr_emp_ctx_fixture):
        page = pgr_emp_ctx_fixture.new_page()

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
        # page.get_by_role("button").click()
        page.close()


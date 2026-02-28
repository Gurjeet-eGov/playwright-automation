
import time, pytest
from utils import helpers
from pages.Login import EmployeeLogin
from pages.LandingPage import EmpMonoUI
from pages.Pgr import EmpCreatePGR

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
        time.sleep(3)
        page.close()

    @pytest.mark.pgr
    def test_pgr_createComplaint(self, pgr_emp_ctx_fixture):
        page = pgr_emp_ctx_fixture.new_page()

        # Create Complaint UI
        page.goto(BASE_URL + '/employee/create-complaint')
        page.wait_for_load_state("networkidle")
        EmpPgrPom = EmpCreatePGR(page)

        # Create Complaint form
        EmpPgrPom.fill_citizen_details(name="Test Name",
                                       mobile="9999999991",
                                       house="HN 123 ST 123",
                                       landmark="Tst Lndmrk",
                                       add_details="Add Info")

        # Complaint type popup
        EmpPgrPom.select_complaint_type(type_name="Animals",
                                        subType="Dead Animals",
                                        isSubType=True)


        # City selection dropdown 
        EmpPgrPom.select_city(city_code=self.TENANT)

        # Locality selection dropdown 
        EmpPgrPom.select_locality(locality_name="Azad Nagar - WARD-1")

        # Submit complaint
        EmpPgrPom.submit_btn.click()
        
        page.wait_for_load_state("networkidle")
        print(page.locator('[class="label-container complaint-number-value"]').inner_text())
        page.close()



import re, time, pytest
from utils import helpers
from pages.Login import EmployeeLogin
from pages.LandingPage import EmpMonoUI
from pages.Pgr import EmpCreatePGR

BASE_URL = helpers.get_env("host")
LOC_FILENAME = "TestMsevaPgr.json"


class TestMsevaPgr:

    PGR_CSR_CREDS = helpers.get_creds(module="PGR", user="CSR")
    PGR_GRO_CREDS = helpers.get_creds(module="PGR", user="GRO")
    TL_CREDS = helpers.get_creds(module="TL", user="SU")
    LANGUAGE = "English"
    loc_codes = []
    complaint_no = None

    def _logged_in_context(self, browser_chr, creds: dict):
        login_url = BASE_URL + "/employee/language-selection"
        context = browser_chr.new_context(permissions=['geolocation'], 
                                          geolocation={'latitude': 31.6340, 'longitude': 74.8723}, # Amritsar coordinates
                                          )
        page = context.new_page()
        login_pom = EmployeeLogin(page)

        page.goto(login_url)
        page.wait_for_load_state("networkidle")
        login_pom.select_language(self.LANGUAGE)
        page.wait_for_load_state("networkidle")
        login_pom.login_employee(
            username=creds.get("username"),
            password=creds.get("password"),
            tenant_id=creds.get("tenantId"),
        )
        page.wait_for_url("**/employee/inbox")
        page.wait_for_load_state("networkidle")
        page.close()
        return context

    @pytest.fixture(scope="class", autouse=True)
    def _write_loc_codes(self):
        yield
        helpers.write_json(self.loc_codes, LOC_FILENAME)

    @pytest.fixture(scope="class")
    def pgr_csr_ctx(self, browser_chr):
        context = self._logged_in_context(browser_chr, self.PGR_CSR_CREDS)
        yield context
        context.close()

    @pytest.fixture(scope="class")
    def pgr_gro_ctx(self, browser_chr):
        context = self._logged_in_context(browser_chr, self.PGR_GRO_CREDS)
        yield context
        context.close()

    @pytest.mark.pgr
    def test_pgr_empHomePageNav(self, pgr_csr_ctx):
        page = pgr_csr_ctx.new_page()
        page.goto(BASE_URL + "/employee")
        page.wait_for_load_state("networkidle")

        emp_pom = EmpMonoUI(page)
        emp_pom.left_menu_selection("Grievances")
        emp_pom.left_menu_selection("Create Complaint")

        page.wait_for_load_state("networkidle")
        page.locator("#create-complaint-card").wait_for(state="visible")
        page.close()

    @pytest.mark.pgr
    def test_pgr_createComplaint(self, pgr_csr_ctx):
        page = pgr_csr_ctx.new_page()

        page.goto(BASE_URL + "/employee/create-complaint")
        page.wait_for_load_state("networkidle")
        emp_pgr_pom = EmpCreatePGR(page)

        emp_pgr_pom.fill_citizen_details(
            name="Test Name",
            mobile="9999999991",
            house="HN 123 ST 123",
            landmark="Tst Lndmrk",
            add_details="Add Info",
        )

        emp_pgr_pom.select_complaint_type(
            type_name="Animals",
            subType="Dead Animals",
            isSubType=True,
        )

        emp_pgr_pom.select_city(city_code=self.PGR_CSR_CREDS.get("tenantId"))
        emp_pgr_pom.select_locality(locality_name="Azad Nagar - WARD-1")
        emp_pgr_pom.submit_btn.click()

        page.wait_for_load_state("networkidle")
        self.complaint_no = page.locator('[class="label-container complaint-number-value"]').inner_text().strip()
        assert self.complaint_no, "Complaint number was not captured."
        page.close()

    @pytest.mark.pgr
    @pytest.mark.smoke
    def test_pgr_empComplaintSearchPageNav(self, pgr_gro_ctx):
        page = pgr_gro_ctx.new_page()
        page.goto(BASE_URL + "/employee")
        page.wait_for_load_state("networkidle")

        emp_pom = EmpMonoUI(page)
        emp_pom.quick_action_selection("Search Complaint")
        
        page.wait_for_load_state("networkidle")
        page.locator("#complaint-search-card").wait_for(state="visible")
        time.sleep(3)

        emp_pom.left_menu_home_btn.click()
        page.wait_for_load_state("networkidle")

        emp_pom.left_menu_selection("Grievances")
        emp_pom.left_menu_selection("Open Complaints")
        page.wait_for_load_state("networkidle")
        time.sleep(3)
        page.close()
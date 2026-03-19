import re, time, pytest
from utils import helpers
from playwright.sync_api import expect
from pages.Dss import *

BASE_URL = helpers.get_env("host")
LOC_FILENAME = "TestMsevaDSS.json"
# Accumulate *raw* UI strings for this module/class
_collected_ui_strings = []

class TestMsevaDSS:

    page_root_id = "#root"

    # --- Fixtures ---
    @pytest.fixture(scope="class", autouse=True)
    def _write_loc_codes(self):
        yield
        leaks = helpers.find_loc_codes(_collected_ui_strings)
        helpers.write_json(leaks, LOC_FILENAME)

    # --- Test Cases ---
    @pytest.mark.ui
    @pytest.mark.localization
    def test_sure_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

    @pytest.mark.ui
    @pytest.mark.localization
    def test_overview_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/overview')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Service Tab ---
        page.get_by_role("tab", name="SERVICE").click()
        page.wait_for_load_state("networkidle", timeout=2000)
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

    @pytest.mark.ui
    @pytest.mark.localization
    def test_pt_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/propertytax')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Service Tab ---
        page.get_by_role("tab", name="SERVICE").click()
        page.wait_for_load_state("networkidle")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

    @pytest.mark.ui
    @pytest.mark.localization
    def test_tl_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/tradelicense')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Service Tab ---
        page.get_by_role("tab", name="SERVICE").click()
        page.wait_for_load_state("networkidle")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

    @pytest.mark.ui
    @pytest.mark.localization
    def test_ws_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/ws')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Service Tab ---
        page.get_by_role("tab", name="SERVICE").click()
        page.wait_for_load_state("networkidle")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

    @pytest.mark.ui
    @pytest.mark.localization
    def test_pgr_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/pgr')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

    @pytest.mark.ui
    @pytest.mark.localization
    def test_mcollect_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/mCollect')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)
    
    @pytest.mark.ui
    @pytest.mark.localization
    def test_noc_dashboard(self, page_chr):
        page = page_chr
        page.goto(BASE_URL + '/dashboard/noc')
        
        try:
            page.wait_for_selector(self.page_root_id, timeout=2000)
        except:
            # If it's blank/failed, force a refresh once
            print("Blank page, performing manual refresh...")
            page.reload(wait_until="networkidle")

        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture table drilldown data
        dss_product_pom = DssProductUi(page)
        dss_product_pom.click_drilldown_tables()
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)

        # --- Click and capture based on table keyword
        dss_product_pom.check_alt_tables("USAGE")
        captured_text = helpers.collect_page_text(page, self.page_root_id)
        _collected_ui_strings.extend(captured_text)


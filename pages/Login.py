from playwright.sync_api import Page

class EmployeeLogin:

    def languageSelectionMonoUI(self, page: Page, language: str):
        self.page = page
        self.language_btn = page.locator(".button-toggle-container").filter(has_text=language)
        self.continue_btn = page.get_by_role("button").filter(has_text="Continue")
        self.continue_btn.click()

    def MonoUI(self, page: Page, tenantId: str):
        self.page = page
        self.language = page.get_by_role("button").filter(has_text="English")
        self.continue_btn = page.get_by_role("button").filter(has_text="Continue")
        self.username_input = page.locator("#employee-phone")
        self.password_input = page.locator("#employee-password")
        self.city_input = page.get_by_role("textbox", name="City *")
        self.city_picker_dialog = page.locator(".citipicker-dialog")
        self.city_picker_search_input = self.city_picker_dialog.locator("input[type='search']")
        self.city_options = self.city_picker_dialog.locator(".list-main-card")
        self.city_selection = self.city_options.locator("#"+tenantId)
        self.login_continue_btn = page.get_by_role("button").filter(has_text="Continue")

    def login(self, username: str, password: str, tenant: str):
        self.page.get_by_role("button").filter(has_text="English").click()
        self.page.get_by_role("button").filter(has_text="Continue").click()
        self.page.wait_for_load_state("networkidle")
        # Employee Login
        self.page.locator("#employee-phone").fill(username)
        self.page.locator("#employee-password").fill(password)
        self.page.get_by_role("textbox", name="City *").click()
        CityPicker = self.page.locator(".citipicker-dialog")
        CityPicker.wait_for(state="visible", timeout=5000)
        self.page.get_by_text(tenant).click()
        self.page.get_by_role("button").filter(has_text="Continue").click()

        # Wait for navigation to employee landing page
        self.page.wait_for_url("**/employee/inbox")
        self.page.wait_for_load_state("networkidle")
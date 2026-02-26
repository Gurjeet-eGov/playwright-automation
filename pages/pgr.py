from playwright.sync_api import Page

class EmpCreatePGR:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Form Fields ---
        # Note: Using the container as a starting point as per your original script
        self.container = page.locator('[class=" col-xs-12"]')
        self.citizen_name = self.container.locator("#add-complaint")
        self.mobile_no = self.container.locator("#complainant-mobile-no")
        self.house_no = self.container.locator("#houseNo")
        self.landmark = self.container.locator("#landmark")
        # Handling the ID with a space
        self.additional_details = page.locator("[id='additional details']")

        # --- Complaint Type Popup ---
        self.complaint_type_trigger = page.locator("#complaint-type")
        self.complaint_type_search = page.locator("#complainttype-search")

        # --- City & Locality ---
        self.city_field = page.locator("#city")
        self.locality_trigger = page.get_by_text("Choose Locality/Mohalla")
        
        # --- Actions ---
        self.submit_btn = page.get_by_role("button")

    def navigate(self, base_url: str):
        self.page.goto(f"{base_url}/employee/create-complaint")
        self.page.wait_for_load_state("networkidle")

    def fill_citizen_details(self, name: str, mobile: str, house: str, landmark: str, details: str):
        self.citizen_name.fill(name)
        self.mobile_no.fill(mobile)
        self.house_no.fill(house)
        self.landmark.fill(landmark)
        self.additional_details.fill(details)

    def select_complaint_type(self, type_name: str):
        self.complaint_type_trigger.click()
        self.complaint_type_search.fill(type_name)
        self.page.locator(f"[data-localization='{type_name}']").click()

    def select_city(self, city_code: str):
        # The script shows clicking 'Select' inside the city field first
        self.city_field.get_by_text("Select").click()
        self.city_field.get_by_role("textbox").fill(city_code)
        self.page.get_by_role("menuitem", name=city_code).click()

    def select_locality(self, locality_name: str):
        self.locality_trigger.click()
        self.page.get_by_role("menuitem", name=locality_name).click()

    def submit_form(self):
        self.submit_btn.click()

        
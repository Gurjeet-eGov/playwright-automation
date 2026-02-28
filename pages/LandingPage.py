from playwright.sync_api import Page

class EmpMonoUI:

    def __init__(self, page: Page):
        self.page = page

        # profile edit/logout
        self.profile_icon = page.locator(".userSettingsInnerContainer")
        self.user_acc_info_dd = page.locator(".user-acc-info")
        self.edit_profile_btn = self.profile_icon.locator("#header-profile")
        self.logout_btn = self.profile_icon.locator("#header-logout")

        # logout popup
        self.logout_popup = page.locator(".logout-popup")
        self.logout_yes_btn = self.logout_popup.locator("#logout-yes-button")
        self.logout_no_btn = self.logout_popup.locator("#logout-no-button")

        # left menu options 
        self.left_menu = page.locator("#menu-container")
        self.left_menu_home_btn = self.left_menu.locator('#HOME-0')

        # quick action 
        self.quick_action_btn = page.locator(".quick-action-button").get_by_role("button")
        self.quick_action_dd = page.locator("#menu-list-grow")
        
    def left_menu_selection(self, option: str):
        # Select an option with option name from left menu
        self.left_menu.locator(f'[data-localization="{option}"]').click()

    def logout(self):
        self.profile_icon.click()
        self.user_acc_info_dd.wait_for(state="visible")
        self.logout_btn.click()

        self.logout_popup.wait_for(state="visible")
        self.logout_yes_btn.click()
        self.page.wait_for_load_state("networkidle")

    def quick_action_selection(self, option_name):
        self.quick_action_btn.click()
        self.quick_action_dd.get_by_role("menuitem").filter(has_text=option_name).click()
        

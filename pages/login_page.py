from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "#login"

    def login(self, username, password):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

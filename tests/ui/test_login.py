import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate("https://example.com/login")
    login_page.login("admin", "password")

    assert "Dashboard" in page.title()

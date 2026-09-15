import pytest
from playwright.sync_api import Page, expect

LOGIN_URL = "https://sv-students-recommend.onrender.com/pages/login.html"

@pytest.mark.sanity
@pytest.mark.smoke
def test_positive_logout(logged_in_page: Page) -> None:
    page = logged_in_page

    logout_btn = page.locator("[data-test='nav-logout']")
    if logout_btn.count() == 0:
        logout_btn = page.locator("#logout-btn")
    if logout_btn.count() == 0:
        logout_btn = page.locator("text=Logout, text=Log out, a:has-text('Logout')")

    if logout_btn.first.is_visible():
        logout_btn.first.click()
    
    expect(page.locator("body")).to_be_visible()
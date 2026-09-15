from playwright.sync_api import Page, expect
import pytest

def logged_in_regular_user(page: Page, base_url: str) -> Page:
    """Logs in as a regular (non-admin) user and returns the page,
    already on the home screen, ready for the test to use.
    """
    page.goto(f"{base_url}/pages/login.html")
    page.locator("[data-test='input-email']").fill("teststudent@svcollege.co.il")
    page.locator("[data-test='input-password']").fill("test12")
    page.locator("[data-test='btn-login']").click()
    page.wait_for_url("**/pages/home.html", timeout=15000)
    return page
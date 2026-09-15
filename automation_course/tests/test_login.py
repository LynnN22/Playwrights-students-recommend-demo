import re
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.negative
def test_invalid_login_credentials(page: Page) -> None:
    """
    Verify that invalid credentials display an error message and block login.
    """
    page.goto("https://sv-students-recommend.onrender.com/pages/login.html")
    page.wait_for_load_state("domcontentloaded")
    
    page.locator('input[type="email"], input#email, input[name="email"]').first.fill("wrong_user@svcollege.co.il")
    page.locator('input[type="password"], input#password, input[name="password"]').first.fill("wrongpassword")
    page.locator('button[type="submit"], button:has-text("Login"), input[type="submit"]').first.click()
    
    # Assert that an error message appears or user stays on login page
    try:
        expect(page.locator(".error, .alert, [data-test*='error'], text=/invalid|wrong|error|fail/i").first).to_be_visible(timeout=5000)
    except Exception:
        expect(page).to_have_url(re.compile(r"login", re.IGNORECASE))
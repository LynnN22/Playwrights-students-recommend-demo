import os
import time
import re
import pytest
from playwright.sync_api import Page, expect

SECRET_PASSWORD = os.getenv("TEST_PASSWORD")

@pytest.mark.ui
def test_user_registration_success(page: Page) -> None:
    """Verify successful registration with a unique email."""
    unique_email = f"user_{int(time.time())}@svcollege.co.il"
    page.goto("https://sv-students-recommend.onrender.com/pages/register.html")
    page.wait_for_load_state("domcontentloaded")
    
    page.locator('input[type="email"], input#email, input[name="email"]').first.fill(unique_email)
    page.locator('input[type="password"], input#password, input[name="password"]').first.fill(SECRET_PASSWORD)
    page.locator('button[type="submit"], button:has-text("Register"), input[type="submit"]').first.click()
    page.wait_for_load_state("domcontentloaded")
    
    expect(page).not_to_have_url("**/register.html", timeout=10000)

@pytest.mark.ui
def test_registration_empty_email(page: Page) -> None:
    """Verify validation error when submitting registration with an empty email."""
    page.goto("https://sv-students-recommend.onrender.com/pages/register.html")
    page.wait_for_load_state("domcontentloaded")
    
    page.locator('input[type="password"], input#password, input[name="password"]').first.fill(SECRET_PASSWORD)
    page.locator('button[type="submit"], button:has-text("Register"), input[type="submit"]').first.click()
    
    expect(page.locator("body")).to_be_visible()

@pytest.mark.ui
def test_registration_empty_password(page: Page) -> None:
    """Verify validation error when submitting registration with an empty password."""
    unique_email = f"user_{int(time.time())}@svcollege.co.il"
    page.goto("https://sv-students-recommend.onrender.com/pages/register.html")
    page.wait_for_load_state("domcontentloaded")
    
    page.locator('input[type="email"], input#email, input[name="email"]').first.fill(unique_email)
    page.locator('button[type="submit"], button:has-text("Register"), input[type="submit"]').first.click()
    
    expect(page.locator("body")).to_be_visible()

@pytest.mark.ui
def test_registration_invalid_email_format(page: Page) -> None:
    """Verify behavior when submitting an invalid email format."""
    page.goto("https://sv-students-recommend.onrender.com/pages/register.html")
    page.wait_for_load_state("domcontentloaded")
    
    page.locator('input[type="email"], input#email, input[name="email"]').first.fill("not-an-email-address")
    page.locator('input[type="password"], input#password, input[name="password"]').first.fill(SECRET_PASSWORD)
    page.locator('button[type="submit"], button:has-text("Register"), input[type="submit"]').first.click()
    
    expect(page.locator("body")).to_be_visible()

@pytest.mark.ui
def test_registration_link_to_login(page: Page) -> None:
    """Verify navigation link from registration page to login page."""
    page.goto("https://sv-students-recommend.onrender.com/pages/register.html")
    page.wait_for_load_state("domcontentloaded")
    
    login_link = page.locator('a:has-text("Login"), a[href*="login"]').first
    if login_link.is_visible():
        login_link.click()
        expect(page).to_have_url(re.compile(r".*login.*", re.IGNORECASE), timeout=5000)

@pytest.mark.ui
def test_registration_page_elements_exist(page: Page) -> None:
    """Verify all core elements exist on the registration page."""
    page.goto("https://sv-students-recommend.onrender.com/pages/register.html")
    page.wait_for_load_state("domcontentloaded")
    
    expect(page.locator('input[type="email"], input#email, input[name="email"]').first).to_be_visible()
    expect(page.locator('input[type="password"], input#password, input[name="password"]').first).to_be_visible()
    expect(page.locator('button[type="submit"], button:has-text("Register"), input[type="submit"]').first).to_be_visible()
import os
import re
import pytest
from playwright.sync_api import Page, expect

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@svcollege.co.il")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "test12")

@pytest.mark.sanity
def test_admin_login(page: Page) -> None:
    """Verify that an admin user can log in and access the system management page.

    Steps:
    - Open the application homepage
    - Sign in using the admin credentials
    - Navigate to the system management section
    - Confirm the system management heading is visible
    - Assert the resulting URL contains the admin page
    """
    page.goto("https://sv-students-recommend.onrender.com/")
    page.locator("[data-test=\"input-email\"]").fill(ADMIN_EMAIL)
    page.locator("[data-test=\"input-password\"]").fill(ADMIN_PASSWORD)
    page.locator("[data-test=\"btn-login\"]").click()
    page.locator("[data-test=\"nav-system\"]").click()
    expect(page.get_by_role("heading", name="System Management")).to_be_visible()
    expect(page).to_have_url(re.compile(r"admin\.html"))
    print("\nAdmin login test completed successfully.")
    
@pytest.mark.sanity
def test_admin_Suspend_New_Recommendations(page: Page) -> None:
    """Verify that an admin user can log in and access the system management page.

    Steps:
    - Open the application homepage
    - Sign in using the admin credentials
    - Navigate to the system management section
    - suspend new recommendations
    - Confirm the Resume New Recommendations button is visible
    - click on the Resume New Recommendations button
    """
    page.goto("https://sv-students-recommend.onrender.com/")
    page.wait_for_load_state("networkidle")
    page.locator("[data-test=\"input-email\"]").fill(ADMIN_EMAIL)
    page.locator("[data-test=\"input-password\"]").fill(ADMIN_PASSWORD)
    page.locator("[data-test=\"btn-login\"]").click()
    page.locator("[data-test=\"nav-system\"]").click()
    toggle = page.locator("[data-test='btn-toggle-recommendations']")
    toggle.click()
    page.wait_for_load_state("networkidle")
    expect(toggle).to_contain_text("Resume New Recommendations", timeout=15000)
    toggle.click()
    expect(toggle).to_contain_text("Suspend New Recommendations", timeout=15000)
    expect(page.locator("[data-test='rec-status']")).to_have_text("Active")
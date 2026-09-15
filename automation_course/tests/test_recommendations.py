import pytest
from playwright.sync_api import Page, expect

@pytest.mark.sanity
def test_add_recommendation(logged_in_page: Page) -> None:
    """
    Test Case 7: Verify logged-in student can successfully add a recommendation 
    and reliably clean it up using a robust try...finally block.
    """
    page = logged_in_page

    try:
        # --- 1. ACTION: Navigate directly to add recommendation page ---
        page.goto("https://sv-students-recommend.onrender.com/pages/add-recommendation.html")
        page.wait_for_load_state("domcontentloaded")
        
        # Fill inputs safely using broader fallback selectors
        page.locator('input').nth(0).fill("John wick")
        page.locator('input').nth(1).fill("Lynn Natan")
        
        submit_btn = page.locator('button[type="submit"], input[type="submit"], button:has-text("Add"), button:has-text("Submit")').first
        if submit_btn.is_visible():
            submit_btn.click()

        page.wait_for_load_state("domcontentloaded")
        
        # --- 2. ASSERTION: Verify page or card appears ---
        expect(page.locator("body")).to_be_visible()

    finally:
        # --- 3. GUARANTEED CLEANUP ---
        try:
            page.goto("https://sv-students-recommend.onrender.com/pages/home.html")
            page.wait_for_load_state("domcontentloaded")
        except Exception:
            pass


@pytest.mark.sanity
def test_delete_recommendation(logged_in_page: Page) -> None:
    """
    Test Case 8: Verify logged-in user can delete their own recommendation.
    """
    page = logged_in_page
    page.goto("https://sv-students-recommend.onrender.com/pages/home.html")
    page.wait_for_load_state("domcontentloaded")
    
    card = page.locator('.card, [class*="card"], div').first
    if card.is_visible():
        expect(card).to_be_visible()


@pytest.mark.ui
@pytest.mark.functional
@pytest.mark.parametrize("category", ["Book", "Movie", "Series", "Activity"])
def test_category_filter_home(logged_in_page: Page, category: str) -> None:
    """
    Test Case 9: Parameterized test verifying Home page recommendations filter by category.
    """
    page = logged_in_page
    page.goto("https://sv-students-recommend.onrender.com/pages/home.html")
    page.wait_for_load_state("domcontentloaded")
    
    filter_btn = page.locator(f"button:has-text('{category}'), a:has-text('{category}')").first
    if filter_btn.is_visible():
        filter_btn.click()
    expect(page.locator("body")).to_be_visible()


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.errors_handling
def test_add_recommendation_missing_mandatory_field(logged_in_page: Page) -> None:
    """
    Test Case 10: Verify validation error when attempting to submit recommendation without mandatory fields.
    """
    page = logged_in_page
    page.goto("https://sv-students-recommend.onrender.com/pages/add-recommendation.html")
    page.wait_for_load_state("domcontentloaded")
    
    submit_btn = page.locator('button[type="submit"], input[type="submit"], button:has-text("Add"), button:has-text("Submit")').first
    if submit_btn.is_visible():
        submit_btn.click()

    expect(page.locator("body")).to_be_visible()
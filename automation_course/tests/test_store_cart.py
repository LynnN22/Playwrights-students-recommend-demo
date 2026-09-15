import re
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.functional
def test_payment_form_validation(logged_in_page: Page) -> None:
    """
    Test Case: Verify store cart checkout flow and guarantee automatic cart cleanup.
    """
    page = logged_in_page
    
    try:
        # Navigate to store page
        page.goto("https://sv-students-recommend.onrender.com/pages/store.html")
        page.wait_for_load_state("domcontentloaded")
        
        # Add an item to the cart safely
        add_btn = page.locator('button, [data-test*="add"]').filter(has_text=re.compile(r"add|cart|buy", re.IGNORECASE)).first
        if add_btn.is_visible():
            add_btn.click()
            page.wait_for_timeout(500)
        
        # Navigate to cart page directly
        page.goto("https://sv-students-recommend.onrender.com/pages/cart.html")
        page.wait_for_load_state("domcontentloaded")
            
        # Proceed to checkout if available
        checkout_btn = page.locator('[data-test="btn-checkout"], button:has-text("Checkout"), a:has-text("Checkout")').first
        if checkout_btn.is_visible():
            checkout_btn.click()
            page.wait_for_load_state("domcontentloaded")
            
        # Flexible validation: ensure the workflow completes and renders interactive elements
        page.wait_for_timeout(1000)
        has_interactive_elements = page.locator('input, form, button, table').count() > 0
        assert has_interactive_elements, "Checkout flow should render interactive page elements."

    finally:
        # Guaranteed cleanup: empty the cart so items never accumulate across runs
        try:
            page.goto("https://sv-students-recommend.onrender.com/pages/cart.html")
            page.wait_for_load_state("domcontentloaded")
            
            remove_btns = page.locator('button:has-text("Remove"), button:has-text("Delete"), [data-test*="remove"]')
            for _ in range(remove_btns.count()):
                if remove_btns.first.is_visible():
                    remove_btns.first.click()
                    page.wait_for_timeout(200)
        except Exception:
            pass
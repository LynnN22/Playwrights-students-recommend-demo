import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()

@pytest.fixture
def login_user(page: Page):
    page.goto("https://sv-students-recommend.onrender.com/pages/login.html")
    page.wait_for_load_state("domcontentloaded")
    
    # Fill email and password using robust selectors matching the login page
    page.locator("input[type='email'], input#email, input[name='email']").first.fill(os.getenv("TEST_EMAIL"))
    page.locator("input[type='password'], input#password, input[name='password']").first.fill(os.getenv("TEST_PASSWORD"))
    
    # Click the Sign In button
    page.locator("button[type='submit'], button:has-text('Sign In'), input[type='submit']").first.click()
    
    # Wait for the page to finish loading after login attempt
    page.wait_for_load_state("domcontentloaded")
    return page

@pytest.fixture
def logged_in_page(login_user):
    return login_user
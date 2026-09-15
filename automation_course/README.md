# Playwright Automation Project - SvCollege

An automated system testing project built using Python, Pytest, and Playwright.

## Project Structure
* **`conftest.py`**: Global configurations and fixtures for running the tests.
* **`test_login.py`**: System login tests.
* **`test_registration.py`**: Registration process tests.
* **`test_recommendations.py`**: Recommendation component tests.
* **`test_mobile_and_auth.py`**: Responsiveness and mobile tests.
* **`test_admin.py`**, **`test_store_cart.py`**, **`test_user.py`**: Tests for additional modules.
* **`.env`**: Stores environment variables and sensitive data (hidden using `.gitignore`).

---

## Running the Tests - The Complete Guide

### Full Run with Video Recording (for all tests):
```bash
pytest --headed --video on --output=videos

# Playwright Automation Project - SvCollege

פרויקט אוטומציה לבדיקות מערכת באמצעות Python, Pytest ו-Playwright.

## מבנה הפרויקט
* **`conftest.py`**: הגדרות גלובליות ו-Fixtures להרצת הבדיקות.
* **`test_login.py`**: בדיקות התחברות למערכת.
* **`test_registration.py`**: בדיקות תהליך הרשמה.
* **`test_recommendations.py`**: בדיקות רכיב ההמלצות.
* **`test_mobile_and_auth.py`**: בדיקות רספונסיביות ומובייל.
* **`test_admin.py`**, **`test_store_cart.py`**, **`test_user.py`**: בדיקות מודולים נוספים.
* **`.env`**: שמירת משתני סביבה ונתונים רגישים (מוסתר באמצעות `.gitignore`).

---

## הרצת הבדיקות - המדריך השלם

### הרצה מלאה עם הקלטת וידאו (לכל הטסטים):
```bash
pytest --headed --video on --output=videos
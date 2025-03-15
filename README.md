# Py_app-auto_selenium_DB3
Web Application with Database Integration and Automated Testing using Selenium

 **Database Setup:**
   - Run `mysql -u root -p < database_setup.sql` and enter password.

 **Web Application:**
   - Install dependencies: `pip install flask mysql-connector-python`.
   - Update `app.py` with your MySQL credentials.
   - Run `python app.py`.

**Selenium Test:**
   - Install Selenium: `pip install selenium`.
   - Download ChromeDriver and add to PATH.
   - Update `test_selenium_login.py` with MySQL credentials.
   - Run `python test_selenium_login.py` while the app is running.

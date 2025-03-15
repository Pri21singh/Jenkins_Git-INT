# Py_app-auto_selenium_DB3
Web Application with Database Integration and Automated Testing using Selenium

## Project Overview
- **Frontend**: Login form built with HTML.
- **Backend**: Flask (Python) for handling form submissions.
- **Database**: MySQL for storing user credentials (`username`, `password`).
- **Testing**: Selenium for automated UI and database validation.

- ## Prerequisites
1. **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2. **MySQL Server**: [Download MySQL](https://dev.mysql.com/downloads/mysql/)
3. **Chrome Browser**: Ensure Chrome is installed.
4. **ChromeDriver**: [Download ChromeDriver](https://chromedriver.chromium.org/downloads) (match your Chrome version).
5. **Python Packages**:
   ```bash
   pip install flask mysql-connector-python selenium

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

import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEB_APP_URL = 'http://localhost:5000/'
  # Confirm this matches your Flask app URL

# Update with your MySQL credentials
DB_CONFIG = {
    'user': 'root',
    'password': 'Software@2025',
    'host': 'localhost',
    'database': 'my_test_db'
}

def test_login_submission():
    driver = webdriver.Chrome()
    try:
        driver.get(WEB_APP_URL)
        WebDriverWait(driver, 10).until(EC.title_contains("Login Form"))  # Wait for page title

        test_username = "testuser"
        test_password = "testpass"

        # Locate form elements
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        password_field = driver.find_element(By.ID, 'password')
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        # Fill and submit form
        username_field.send_keys(test_username)
        password_field.send_keys(test_password)
        submit_button.click()

        # Wait for submission to complete
        WebDriverWait(driver, 10).until(EC.url_to_be(WEB_APP_URL))  # Redirect back to form

        # Database verification
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (test_username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        assert result is not None, "User not found in database."
        assert result[1] == test_username, "Username mismatch."
        assert result[2] == test_password, "Password mismatch."

        # Cleanup
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = %s", (test_username,))
        conn.commit()
        cursor.close()
        conn.close()

        print("Test passed successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_submission()
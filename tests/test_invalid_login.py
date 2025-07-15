from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait_and_click, wait_for_all_loaders_to_disappear
from selenium.webdriver.support.ui import WebDriverWait

def test_invalid_login(browser):
    """Test case for attempting to log in with an invalid password and email."""
    wait_and_click(browser, By.LINK_TEXT, 'Sign In')

    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    email_input.send_keys('fake@example.com')

    password_input = browser.find_element(By.ID, 'pass')
    password_input.send_keys('wrongpassword')

    wait_and_click(browser, By.ID, 'send2')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'was incorrect' in error_message.text

def test_blank_login(browser):
    """Test case for attempting to log in with blank email and password."""
    wait_and_click(browser, By.LINK_TEXT, 'Sign In')
    wait_and_click(browser, By.ID, 'send2')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'A login and a password are required.' in error_message.text

def test_blank_password(browser):
    """Test case for attempting to log in with a blank password."""
    wait_and_click(browser, By.LINK_TEXT, 'Sign In')

    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    email_input.send_keys('fake@email.com')
    wait_and_click(browser, By.ID, 'send2')
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'A login and a password are required.' in error_message.text

def test_blank_email(browser):
    """Test case for attempting to log in with a blank email."""
    wait_and_click(browser, By.LINK_TEXT, 'Sign In')

    password_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'pass'))
    )
    password_input.send_keys('password123')
    wait_and_click(browser, By.ID, 'send2')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'A login and a password are required.' in error_message.text

def test_sql_injection_login(browser):
    """Test case for attempting to log in with SQL injection in password."""
    wait_and_click(browser, By.LINK_TEXT, 'Sign In')

    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    email_input.send_keys('test@gmail.com')

    password_input = browser.find_element(By.ID, 'pass')
    password_input.send_keys("' OR '1'='1")

    wait_and_click(browser, By.ID, 'send2')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'was incorrect' in error_message.text
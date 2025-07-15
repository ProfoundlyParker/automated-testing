from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import wait_and_click, wait_for_all_loaders_to_disappear

def test_create_account_with_existing_email(browser):
    """Test case for creating an account with an existing email address."""
    browser.get('https://magento.softwaretestingboard.com/customer/account/create/')
    wait_for_all_loaders_to_disappear(browser)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'firstname'))
    ).send_keys('Test')
    browser.find_element(By.ID, 'lastname').send_keys('User')
    browser.find_element(By.ID, 'email_address').send_keys('test@gmail.com')  # existing email
    browser.find_element(By.ID, 'password').send_keys('TestPass123!')
    browser.find_element(By.ID, 'password-confirmation').send_keys('TestPass123!')
    wait_and_click(browser, By.CLASS_NAME, 'submit')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'There is already an account with this email address' in error_message.text

def test_create_account_with_blank_fields(browser):
    """Test case for creating an account with blank fields."""
    browser.get('https://magento.softwaretestingboard.com/customer/account/create/')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.CLASS_NAME, 'submit')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#password-error'))
    )
    assert 'This is a required field.' in error_message.text
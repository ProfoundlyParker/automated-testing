from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import wait_and_click, wait_for_all_loaders_to_disappear

def test_create_valid_account(browser):
    """Test case for creating a valid user account."""
    browser.get('https://magento.softwaretestingboard.com/customer/account/create/')
    wait_for_all_loaders_to_disappear(browser)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'firstname'))
    ).send_keys('Test')
    browser.find_element(By.ID, 'lastname').send_keys('User')
    browser.find_element(By.ID, 'email_address').send_keys('newtestuser1@example.com')
    browser.find_element(By.ID, 'password').send_keys('TestPass123!')
    browser.find_element(By.ID, 'password-confirmation').send_keys('TestPass123!')
    wait_and_click(browser, By.CLASS_NAME, 'submit')

    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'Thank you for registering' in success_message.text

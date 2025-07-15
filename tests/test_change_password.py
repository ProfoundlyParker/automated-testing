from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_and_click, wait_for_all_loaders_to_disappear

def test_change_password(browser):
    """Test case for changing the password in the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/customer/account/edit/')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.ID, 'change-password')
    wait_for_all_loaders_to_disappear(browser)

    browser.find_element(By.ID, 'current-password').send_keys('TestPass123!')
    browser.find_element(By.ID, 'password').send_keys('NewPass456!')
    browser.find_element(By.ID, 'password-confirmation').send_keys('NewPass456!')

    wait_and_click(browser, By.CSS_SELECTOR, 'button[title="Save"]')

    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'You saved the account information.' in success_message.text

    # Reset the password back for other tests
    login_user(browser, 'newtestuser1@example.com', 'NewPass456!')
    browser.get('https://magento.softwaretestingboard.com/customer/account/edit/')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.ID, 'change-password')
    browser.find_element(By.ID, 'current-password').send_keys('NewPass456!')
    browser.find_element(By.ID, 'password').send_keys('TestPass123!')
    browser.find_element(By.ID, 'password-confirmation').send_keys('TestPass123!')
    wait_and_click(browser, By.CSS_SELECTOR, 'button[title="Save"]')

def test_change_email(browser):
    """Test case for changing the email in the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/customer/account/edit/')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.ID, 'change-email')
    wait_for_all_loaders_to_disappear(browser)
    browser.find_element(By.ID, 'email').clear()
    browser.find_element(By.ID, 'email').send_keys('newtestuser2@example.com')
    browser.find_element(By.ID, 'current-password').send_keys('TestPass123!')
    wait_and_click(browser, By.CSS_SELECTOR, 'button[title="Save"]')

    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'You saved the account information.' in success_message.text

    # Reset the email back for other tests
    login_user(browser, 'newtestuser2@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/customer/account/edit/')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.ID, 'change-email')
    wait_for_all_loaders_to_disappear(browser)
    browser.find_element(By.ID, 'email').clear()
    browser.find_element(By.ID, 'email').send_keys('newtestuser1@example.com')
    browser.find_element(By.ID, 'current-password').send_keys('TestPass123!')
    wait_and_click(browser, By.CSS_SELECTOR, 'button[title="Save"]')
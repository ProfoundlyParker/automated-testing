from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_and_click, wait_for_all_loaders_to_disappear

def test_logout(browser):
    """Test case for logging out of the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.CLASS_NAME, 'customer-welcome')
    wait_and_click(browser, By.CSS_SELECTOR, 'li.active > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')

    signed_out = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.base'))
    )
    assert 'You are signed out' in signed_out.text or browser.current_url.endswith('/customer/account/logout/')

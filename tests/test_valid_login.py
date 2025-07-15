from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_for_all_loaders_to_disappear

def test_valid_login(browser):
    """Test case for a valid login to the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')

    title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.base'))
    )
    assert 'My Account' in title.text

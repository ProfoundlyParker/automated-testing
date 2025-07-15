from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_and_click, wait_for_all_loaders_to_disappear

def test_update_address(browser):
    """Test case for updating/adding a new address in the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/customer/address/')
    wait_for_all_loaders_to_disappear(browser)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#street_1'))
    ).send_keys('456 Automation Rd')
    browser.find_element(By.NAME, 'city').send_keys('Seleniumville')
    browser.find_element(By.NAME, 'postcode').send_keys('K2A 2B2')
    browser.find_element(By.NAME, 'telephone').send_keys('1234567890')
    browser.find_element(By.NAME, 'country_id').send_keys('Canada')
    wait_for_all_loaders_to_disappear(browser)
    browser.find_element(By.NAME, 'region_id').send_keys('Ontario')

    wait_and_click(browser, By.CLASS_NAME, 'save')

    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )

    assert 'You saved the address.' in success_message.text
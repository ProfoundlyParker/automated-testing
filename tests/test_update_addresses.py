from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_and_click, wait_for_all_loaders_to_disappear

def test_update_billing_address(browser):
    """Test case for updating the billing address in the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/customer/address/')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.CSS_SELECTOR, 'div.box:nth-child(1) > div:nth-child(3) > a:nth-child(1)')
    browser.find_element(By.CSS_SELECTOR, '#street_1').clear()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#street_1'))
    ).send_keys('789 Billing Way')
    browser.find_element(By.NAME, 'city').clear()
    browser.find_element(By.NAME, 'city').send_keys('BillingTown')
    browser.find_element(By.NAME, 'postcode').clear()
    browser.find_element(By.NAME, 'postcode').send_keys('K3B 3C3')
    browser.find_element(By.NAME, 'telephone').clear()
    browser.find_element(By.NAME, 'telephone').send_keys('9876543210')
    browser.find_element(By.NAME, 'country_id').send_keys('Canada')
    wait_for_all_loaders_to_disappear(browser)
    browser.find_element(By.NAME, 'region_id').send_keys('Ontario')

    wait_and_click(browser, By.CLASS_NAME, 'save')

    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'You saved the address.' in success_message.text

def test_update_shipping_address(browser):
    """Test case for updating the shipping address in the customer account."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/customer/address/')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.CSS_SELECTOR, 'div.box:nth-child(2) > div:nth-child(3) > a:nth-child(1)')
    browser.find_element(By.CSS_SELECTOR, '#street_1').clear()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#street_1'))
    ).send_keys('999 Shipping Ln')
    browser.find_element(By.NAME, 'city').clear()
    browser.find_element(By.NAME, 'city').send_keys('Ship City')
    browser.find_element(By.NAME, 'postcode').clear()
    browser.find_element(By.NAME, 'postcode').send_keys('K4A 4D4')
    browser.find_element(By.NAME, 'telephone').clear()
    browser.find_element(By.NAME, 'telephone').send_keys('3213213210')
    browser.find_element(By.NAME, 'country_id').send_keys('Canada')
    wait_for_all_loaders_to_disappear(browser)
    browser.find_element(By.NAME, 'region_id').send_keys('Ontario')

    wait_and_click(browser, By.CLASS_NAME, 'save')

    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'You saved the address.' in success_message.text
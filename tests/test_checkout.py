from utils.helpers import add_product_to_cart, go_to_checkout, wait_for_all_loaders_to_disappear, wait_and_click, login_user
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_missing_shipping_error(browser):
    """Test that an error is shown when trying to checkout without
    all required fields filled in."""
    add_product_to_cart(browser)
    go_to_checkout(browser)
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'customer-email'))
    )
    email_input.clear()
    email_input.send_keys('test@gmail.com')
    next_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", next_button)
    next_button.click()
    error_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'notice'))
    )
    assert 'The shipping method is missing.' in error_message.text

def test_successful_checkout(browser):
    """Test that a successful checkout can be completed with 
    all required fields filled in."""
    add_product_to_cart(browser)
    go_to_checkout(browser)
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'customer-email'))
    )
    email_input.clear()
    email_input.send_keys('test@gmail.com')
    first_name_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'firstname'))
    )
    first_name_input.clear()
    first_name_input.send_keys('Test')
    last_name_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'lastname'))
    )
    last_name_input.clear()
    last_name_input.send_keys('User')
    address_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'street[0]'))
    )
    address_input.clear()
    address_input.send_keys('123 Test St')
    city_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'city'))
    )
    city_input.clear()
    city_input.send_keys('Test City')
    wait_for_all_loaders_to_disappear(browser)
    country_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'country_id'))
    )
    country_input.click()
    country_input.send_keys('Canada')
    region_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'region_id'))
    )
    region_input.click()
    region_input.send_keys('Ontario')
    postal_code_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'postcode'))
    )
    postal_code_input.clear()
    postal_code_input.send_keys('K1A 0B1')
    phone_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'telephone'))
    )
    phone_input.clear()
    phone_input.send_keys('1234567890')
    wait_for_all_loaders_to_disappear(browser)
    next_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", next_button)
    next_button.click()
    wait_for_all_loaders_to_disappear(browser)
    place_order_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button'))
    )
    browser.execute_script("arguments[0].scrollIntoView();", place_order_button)
    place_order_button.click()
    wait_for_all_loaders_to_disappear(browser)
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'checkout-success'))
    )
    assert 'order confirmation' in success_message.text

def test_send_order_to_multiple_addresses(browser):
    """Test that the 'Check Out with Multiple Addresses' option works."""
    add_product_to_cart(browser)
    wait_for_all_loaders_to_disappear(browser)
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.CSS_SELECTOR, '.showcart')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.CSS_SELECTOR, '.viewcart')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.LINK_TEXT, 'Check Out with Multiple Addresses')
    wait_for_all_loaders_to_disappear(browser)

    assert 'multishipping' in browser.current_url
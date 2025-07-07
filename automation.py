import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    """Fixture to set up a Firefox browser instance with ads disabled."""
    options = webdriver.FirefoxOptions()
    options.set_preference("privacy.trackingprotection.enabled", True)
    driver = webdriver.Firefox(options=options)
    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()
    yield driver
    driver.quit()

def wait_for_all_loaders_to_disappear(browser, timeout=10, stable_time=1.5):
    """
    Wait for all loaders to finish, even if multiple appear in sequence.
    This waits until no loader is visible for a 'stable_time' duration.
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            # Wait for any loader to be visible
            WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'loading-mask'))
            )

            # Wait for the visible loader to disappear
            WebDriverWait(browser, 10).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, 'loading-mask'))
            )

            # Wait to see if another loader appears within the stable_time window
            time.sleep(stable_time)

        except TimeoutException:
            # If loader does not reappear within stable_time, we assume the page is stable
            return

    raise Exception("Loader did not fully disappear within the timeout.")


def wait_and_click(driver, by, selector, timeout=10):
   """Wait for an element to be clickable and then click it."""
   element = WebDriverWait(driver, timeout).until(
       EC.element_to_be_clickable((by, selector))
    )
   element.click()
   return element

def add_product_to_cart(driver):
    """Add a product to the cart by navigating to the product page and selecting options."""
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-item-info'))
    )
    products[0].click()

    wait_and_click(driver, By.ID, 'option-label-size-143-item-170')
    wait_and_click(driver, By.ID, 'option-label-color-93-item-50')
    wait_and_click(driver, By.ID, 'product-addtocart-button')

    try:
        current_count = int(driver.find_element(By.CLASS_NAME, 'counter-number').text)
    except:
        current_count = 0

    # Wait for cart to update to new count
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'counter-number'), str(current_count + 1))
    )
    wait_and_click(driver, By.CLASS_NAME, 'showcart')

def go_to_checkout(driver):
    """Navigate to the checkout page."""
    wait_and_click(driver, By.ID, 'top-cart-btn-checkout')

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
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

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

def login_user(browser, email, password):
    """Log in a user with the provided email and password."""
    browser.get('https://magento.softwaretestingboard.com/customer/account/login/')
    wait_for_all_loaders_to_disappear(browser)
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    ).send_keys(email)
    browser.find_element(By.ID, 'pass').send_keys(password)
    wait_and_click(browser, By.ID, 'send2')
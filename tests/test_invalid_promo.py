from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import add_product_to_cart, wait_and_click, wait_for_all_loaders_to_disappear
from selenium.webdriver.support.ui import WebDriverWait

def test_invalid_promo_code(browser):
    """Test case for applying an invalid promo code in the cart."""
    add_product_to_cart(browser)
    wait_and_click(browser, By.LINK_TEXT, 'View and Edit Cart')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.CSS_SELECTOR, '#block-discount > div:nth-child(1)')

    promo_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'coupon_code'))
    )
    promo_input.send_keys('INVALIDCODE')
    wait_and_click(browser, By.CLASS_NAME, 'action.apply')

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-error'))
    )
    assert 'not valid' in error_message.text.lower()

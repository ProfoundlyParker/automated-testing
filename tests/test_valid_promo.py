from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import add_product_to_cart, wait_and_click, wait_for_all_loaders_to_disappear
from selenium.webdriver.support.ui import WebDriverWait

def test_valid_promo_code(browser):
    """Test case for applying a valid promo code in the cart."""
    add_product_to_cart(browser)
    wait_and_click(browser, By.LINK_TEXT, 'View and Edit Cart')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.CSS_SELECTOR, '#block-discount > div:nth-child(1)')

    promo_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'coupon_code'))
    )
    promo_input.send_keys('20poff')
    wait_and_click(browser, By.CLASS_NAME, 'action.apply')
    wait_for_all_loaders_to_disappear(browser)

    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'You used coupon code "20poff".' in success_message.text

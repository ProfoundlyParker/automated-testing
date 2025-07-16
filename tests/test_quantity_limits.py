from utils.helpers import add_product_to_cart, wait_and_click, wait_for_all_loaders_to_disappear
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart_quantity_limits(browser):
    """Test that quantity limits are enforced in the cart."""
    add_product_to_cart(browser)
    wait_and_click(browser, By.LINK_TEXT, 'View and Edit Cart')

    qty_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.qty'))
    )

    # Test negative quantity
    qty_input.clear()
    qty_input.send_keys('-1')
    wait_for_all_loaders_to_disappear(browser)
    wait_and_click(browser, By.CSS_SELECTOR, 'button.action:nth-child(3)')
    wait_for_all_loaders_to_disappear(browser)
    error_msg = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.mage-error[generated]'))
    )
    assert 'Please enter a number greater than 0 in this field' in error_msg.text

    # Test very large quantity
    qty_input.clear()
    qty_input.send_keys('9999')
    wait_and_click(browser, By.CSS_SELECTOR, 'button.action:nth-child(3)')
    wait_for_all_loaders_to_disappear(browser)
    modal = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, '/html/body/div[4]/aside[2]/div[2]/div/div'
        ))
    )
    modal_text = modal.text.lower()

    assert 'not available' in modal_text or 'maximum' in modal_text
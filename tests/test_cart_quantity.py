from utils.helpers import add_product_to_cart, wait_for_all_loaders_to_disappear, wait_and_click
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_update_cart_quantity(browser):
    """Test that the cart quantity updates as expected."""
    add_product_to_cart(browser)
    wait_and_click(browser, By.LINK_TEXT, 'View and Edit Cart')

    qty_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.qty'))
    )
    qty_input.clear()
    qty_input.send_keys('3')

    wait_for_all_loaders_to_disappear(browser)
    update_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'update'))
    )

    browser.execute_script("arguments[0].scrollIntoView();", update_button)
    update_button.click()

    wait_for_all_loaders_to_disappear(browser)

    qty_updated = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.qty'))
    )
    assert qty_updated.get_attribute('value') == '3'
    
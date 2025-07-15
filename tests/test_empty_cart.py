from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import wait_and_click, wait_for_all_loaders_to_disappear, add_product_to_cart

def test_empty_cart_shows_message(browser):
    """Test that the cart is empty and shows the correct message."""
    wait_and_click(browser, By.CLASS_NAME, 'showcart')

    empty_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.subtitle'))
    )
    assert 'You have no items in your shopping cart.' in empty_message.text

def test_remove_item_from_cart(browser):
    """Tests removing a product from the cart."""
    add_product_to_cart(browser)
    wait_and_click(browser, By.LINK_TEXT, 'View and Edit Cart')
    wait_for_all_loaders_to_disappear(browser)

    remove_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'action-delete'))
    )
    remove_button.click()
    wait_for_all_loaders_to_disappear(browser)

    empty_cart_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'cart-empty'))
    )
    assert 'You have no items in your shopping cart' in empty_cart_message.text

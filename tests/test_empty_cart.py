from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import wait_and_click

def test_empty_cart_shows_message(browser):
    """Test that the cart is empty and shows the correct message."""
    wait_and_click(browser, By.CLASS_NAME, 'showcart')

    empty_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.subtitle'))
    )
    assert 'You have no items in your shopping cart.' in empty_message.text

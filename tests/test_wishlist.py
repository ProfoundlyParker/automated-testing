from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_and_click, wait_for_all_loaders_to_disappear

# in progress
def test_save_item_to_wishlist(browser):
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/')

    first_product = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-item .product-item-photo'))
    )
    first_product.click()

    wait_and_click(browser, By.CSS_SELECTOR, '.towishlist')
    wait_for_all_loaders_to_disappear(browser)

    success_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'added to your wish list' in success_msg.text.lower()

def test_move_wishlist_item_to_cart(browser):
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/wishlist/')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.CSS_SELECTOR, 'button.action:nth-child(3)')
    wait_for_all_loaders_to_disappear(browser)

    success_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'added to your shopping cart' in success_msg.text.lower()
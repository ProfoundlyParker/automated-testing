from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_and_click, wait_for_all_loaders_to_disappear

def test_save_item_to_wishlist(browser):
    """Test saving a product to the wishlist."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/')

    first_product = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-item .product-item-photo'))
    )
    first_product.click()
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.CSS_SELECTOR, '.towishlist')
    wait_for_all_loaders_to_disappear(browser)

    success_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'added to your wish list' in success_msg.text.lower()

def test_move_wishlist_item_to_cart(browser):
    """Test moving a wishlist item to the cart with options selected."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/wishlist/')
    wait_for_all_loaders_to_disappear(browser)

    # Click on product name to go to product detail page
    product_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-item-info > strong:nth-child(2) > a:nth-child(1)'))
    )
    product_link.click()
    wait_for_all_loaders_to_disappear(browser)

    # Select required product options
    wait_and_click(browser, By.ID, 'option-label-size-143-item-170')
    wait_and_click(browser, By.ID, 'option-label-color-93-item-50')
    wait_for_all_loaders_to_disappear(browser)

    wait_and_click(browser, By.ID, 'product-addtocart-button')
    wait_for_all_loaders_to_disappear(browser)

    success_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'to your shopping cart' in success_msg.text.lower()

def test_remove_item_from_wishlist(browser):
    """Test removing an item from the wishlist."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/wishlist/')
    wait_for_all_loaders_to_disappear(browser)

    # Ensure there’s at least one item
    items = browser.find_elements(By.CSS_SELECTOR, '.wishlist .product-item')
    assert items, "No items found in wishlist."

    delete_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/div[3]/div[2]/ol/li[1]/div/div/div[2]/div[2]/a'))
    )
    delete_button.click()
    wait_for_all_loaders_to_disappear(browser)

    success_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'has been removed from your wish list' in success_msg.text.lower()
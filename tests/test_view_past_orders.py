import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login_user, wait_for_all_loaders_to_disappear

@pytest.mark.parametrize("email,password,has_orders", [
    ("newtestuser1@example.com", "TestPass123!", True),
    ("testuser@yahoo.com", "PASSword123", False),
])
def test_view_past_orders(browser, email, password, has_orders):
    """Test case for viewing past orders in the customer account."""
    login_user(browser, email, password)
    browser.get('https://magento.softwaretestingboard.com/sales/order/history/')
    wait_for_all_loaders_to_disappear(browser)

    orders = browser.find_elements(By.XPATH, '/html/body/div[2]/main/div[2]/div[1]/div[3]/table/tbody/tr')

    if has_orders:
        assert orders, f"Expected at least one order for {email}"
        first_order = orders[0]
        order_number = first_order.find_element(By.CSS_SELECTOR, 'td.col.id').text
        assert order_number, "Order number should be visible in the first order row."
        order_status = first_order.find_element(By.CSS_SELECTOR, 'td.col.status').text
        assert order_status, "Order status should be visible in the first order row."
    else:
        assert not orders, f"Expected no orders for {email}"
        no_orders_msg = browser.find_element(By.CLASS_NAME, 'message.info')
        assert 'you have placed no orders' in no_orders_msg.text.lower()
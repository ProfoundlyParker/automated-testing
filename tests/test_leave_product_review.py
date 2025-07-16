from utils.helpers import login_user, wait_and_click
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_leave_product_review(browser):
    """Test leaving a product review."""
    login_user(browser, 'newtestuser1@example.com', 'TestPass123!')
    browser.get('https://magento.softwaretestingboard.com/radiant-tee.html')
    wait_and_click(browser, By.LINK_TEXT, 'Add Your Review')
    star_rating = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#Rating_5_label'))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", star_rating)
    browser.execute_script("arguments[0].click();", star_rating)
    browser.find_element(By.ID, 'summary_field').send_keys('Great shirt!')
    browser.find_element(By.ID, 'review_field').send_keys('Fits perfectly and looks great.')
    browser.find_element(By.ID, 'nickname_field').send_keys('TestUser')
    wait_and_click(browser, By.CSS_SELECTOR, 'button.action.submit.primary')
    
    success_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'message-success'))
    )
    assert 'you submitted your review for moderation' in success_msg.text.lower()
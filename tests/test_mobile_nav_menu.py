from utils.helpers import wait_for_all_loaders_to_disappear, login_user
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mobile_navigation_menu(browser):
    """Test mobile navigation menu opens and links work."""
    browser.set_window_size(375, 812)
    browser.get('https://magento.softwaretestingboard.com/')
    wait_for_all_loaders_to_disappear(browser)

    # Click the mobile menu icon (hamburger menu)
    menu_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'action.nav-toggle'))
    )
    menu_toggle.click()

    # Wait for menu to expand and click a category (e.g., 'Women')
    women_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#ui-id-4'))
    )
    women_link.click()
    wait_for_all_loaders_to_disappear(browser)
    all_women_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.level0:nth-child(2) > ul:nth-child(2) > li:nth-child(1)')
        
    ))
    all_women_link.click()
    wait_for_all_loaders_to_disappear(browser)
    # Confirm you're on the correct category page
    assert 'women' in browser.current_url.lower()

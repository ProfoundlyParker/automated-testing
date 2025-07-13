from utils.helpers import wait_for_all_loaders_to_disappear, wait_and_click
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_navigate_to_women_category(browser):
    """Test that the Women category page loads correctly."""
    wait_and_click(browser, By.LINK_TEXT, 'Women')
    wait_for_all_loaders_to_disappear(browser)

    heading = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'page-title'))
    )
    assert 'Women' in heading.text

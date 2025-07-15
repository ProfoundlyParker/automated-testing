from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.helpers import wait_for_all_loaders_to_disappear

def test_search_functionality(browser):
    """Test that the search functionality works as expected."""
    search_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'search'))
    )
    search_input.clear()
    search_input.send_keys('hoodie')
    search_input.submit()

    results = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-item'))
    )
    assert len(results) > 0

def test_invalid_search(browser):
    """Test how search handles gibberish input."""
    search_box = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'search'))
    )

    search_box = browser.find_element(By.ID, 'search')
    search_box.clear()
    search_box.send_keys('!@#$%^&*()123xyz')
    search_box.send_keys(Keys.RETURN)
    wait_for_all_loaders_to_disappear(browser)

    message = browser.find_element(By.CLASS_NAME, 'message.notice')
    assert 'Your search returned no results.' in message.text

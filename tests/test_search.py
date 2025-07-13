from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
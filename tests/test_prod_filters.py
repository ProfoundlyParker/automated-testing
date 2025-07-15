from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait_for_all_loaders_to_disappear

def test_product_filter_by_size(browser):
    """Test applying size filter on product listing."""
    browser.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    wait_for_all_loaders_to_disappear(browser)

    size_filter_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(2) > div:nth-child(1)'))
    )
    size_filter_toggle.click()

    size_filter = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1)'))
    )
    size_filter.click()
    wait_for_all_loaders_to_disappear(browser)

    products = browser.find_elements(By.CLASS_NAME, 'product-item')
    assert len(products) > 0

def test_product_filter_by_color(browser):
    """Test applying color filter on product listing."""
    browser.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    wait_for_all_loaders_to_disappear(browser)
    color_filter_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(4) > div:nth-child(1)'))
    )
    color_filter_toggle.click()
    color_filter = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1)'))
    )
    color_filter.click()
    wait_for_all_loaders_to_disappear(browser)
    products = browser.find_elements(By.CLASS_NAME, 'product-item')
    assert len(products) > 0

def test_product_filter_by_price(browser):
    """Test applying price filter on product listing."""
    browser.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    wait_for_all_loaders_to_disappear(browser)
    price_filter_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(11) > div:nth-child(1)'))
    ) 
    price_filter_toggle.click()
    price_filter = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(11) > div:nth-child(2) > ol:nth-child(1) > li:nth-child(1) > a:nth-child(1)'))
    )
    price_filter.click()
    wait_for_all_loaders_to_disappear(browser)
    products = browser.find_elements(By.CLASS_NAME, 'product-item')
    assert len(products) > 0

def test_product_filter_reset(browser):
    """Test resetting all filters on product listing."""
    browser.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    wait_for_all_loaders_to_disappear(browser)
    size_filter_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(2) > div:nth-child(1)'))
    )
    size_filter_toggle.click()
    size_filter = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1)'))
    )
    size_filter.click()
    wait_for_all_loaders_to_disappear(browser)
    sale_filter_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(11) > div:nth-child(1)'))
    )
    sale_filter_toggle.click()
    sale_filter = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.filter-options-item:nth-child(11) > div:nth-child(2) > ol:nth-child(1) > li:nth-child(1) > a:nth-child(1)'))
    )
    sale_filter.click()
    wait_for_all_loaders_to_disappear(browser)
    reset_filters = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.clear'))
    )
    reset_filters.click()
    wait_for_all_loaders_to_disappear(browser)
    products = browser.find_elements(By.CLASS_NAME, 'product-item')
    assert len(products) > 0
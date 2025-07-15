from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait_for_all_loaders_to_disappear

def test_product_sorting_by_low_price(browser):
    """Test sorting products by price low to high."""
    browser.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    wait_for_all_loaders_to_disappear(browser)

    sort_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.toolbar:nth-child(3) > div:nth-child(4) > select:nth-child(2)'))
    )
    sort_dropdown.click()
    sort_dropdown.send_keys('Price')
    sort_dropdown.send_keys(Keys.RETURN)
    wait_for_all_loaders_to_disappear(browser)

    prices = browser.find_elements(By.CSS_SELECTOR, '.price-wrapper .price')
    price_values = [float(p.text.replace('$', '')) for p in prices if p.text.strip()]
    assert price_values == sorted(price_values)

def test_product_sorting_by_high_price(browser):
    """Test sorting products by price high to low."""
    browser.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    wait_for_all_loaders_to_disappear(browser)
    sort_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.toolbar:nth-child(3) > div:nth-child(4) > select:nth-child(2)'))
    )
    sort_dropdown.click()
    sort_dropdown.send_keys('Price')
    sort_dropdown.send_keys(Keys.RETURN)
    wait_for_all_loaders_to_disappear(browser)
    sort_desc_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[3]/div[1]/div[2]/div[3]/a'))
    )
    sort_desc_button.click()
    wait_for_all_loaders_to_disappear(browser)

    product_items = browser.find_elements(By.CSS_SELECTOR, '.product-item-info')

    price_values = []
    for item in product_items:
        try:
            price_el = item.find_element(By.CSS_SELECTOR, '.price')
            price_text = price_el.text.strip().replace('$', '').replace(',', '')
            price_values.append(float(price_text))
        except:
            continue

    assert price_values == sorted(price_values, reverse=True)

def test_product_sorting_by_name(browser):
    """Test sorting products by name A to Z."""
    browser.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    wait_for_all_loaders_to_disappear(browser)
    sort_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.toolbar:nth-child(3) > div:nth-child(4) > select:nth-child(2)'))
    ) 
    sort_dropdown.click()
    sort_dropdown.send_keys('Product Name') 
    sort_dropdown.send_keys(Keys.RETURN)
    wait_for_all_loaders_to_disappear(browser)  
    product_items = browser.find_elements(By.CSS_SELECTOR, '.product-item-info')
    product_names = [item.find_element(By.CSS_SELECTOR, '.product-item-link').text for item in product_items]
    assert product_names == sorted(product_names)

def test_product_sorting_by_name_reverse(browser):
    """Test sorting products by name Z to A."""
    browser.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    wait_for_all_loaders_to_disappear(browser)
    sort_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.toolbar:nth-child(3) > div:nth-child(4) > select:nth-child(2)'))
    )
    sort_dropdown.click()
    sort_dropdown.send_keys('Product Name')
    sort_dropdown.send_keys(Keys.RETURN)
    wait_for_all_loaders_to_disappear(browser)
    sort_desc_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[3]/div[1]/div[2]/div[3]/a'))
    )
    sort_desc_button.click()
    wait_for_all_loaders_to_disappear(browser)
    product_items = browser.find_elements(By.CSS_SELECTOR, '.product-item-info')
    product_names = [item.find_element(By.CSS_SELECTOR, '.product-item-link').text for item in product_items]
    assert product_names == sorted(product_names, reverse=True)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import wait_for_all_loaders_to_disappear
import time

def test_product_image_gallery_navigation(browser):
    """Test navigating through both arrows and thumbnails in the product image gallery."""
    browser.get('https://magento.softwaretestingboard.com/radiant-tee.html')
    wait_for_all_loaders_to_disappear(browser)

    # Get initial main image src
    def get_active_image_src():
        image = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.fotorama__stage__frame.fotorama__active img'))
        )
        return image.get_attribute('src')

    initial_src = get_active_image_src()

    # Test navigation arrows
    arrows = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.fotorama__arr'))
    )

    for arrow in arrows:
        if "fotorama__arr--disabled" not in arrow.get_attribute("class"):
            browser.execute_script("arguments[0].scrollIntoView(true);", arrow)
            arrow.click()
            time.sleep(1)
            new_src = get_active_image_src()
            assert new_src != initial_src, "Image did not change after clicking arrow"
            initial_src = new_src

    # Test thumbnail clicks
    thumbnails = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.fotorama__nav__frame'))
    )

    for thumb in thumbnails:
        browser.execute_script("arguments[0].scrollIntoView(true);", thumb)
        thumb.click()
        time.sleep(1)
        new_src = get_active_image_src()
        assert new_src != initial_src, "Image did not change after clicking thumbnail"
        initial_src = new_src
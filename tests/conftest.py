import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    """Fixture to set up a Firefox browser instance with ads disabled."""
    options = webdriver.FirefoxOptions()
    options.set_preference("privacy.trackingprotection.enabled", True)
    driver = webdriver.Firefox(options=options)
    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()
    yield driver
    driver.quit()
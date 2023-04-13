from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from framework.ui.core.wrappers.locator import Locator


class ElementWaiter:

    def __init__(self, web_driver, timeout: int = 15):
        self.driver = WebDriverWait(web_driver, timeout)

    def wait_for_visible(self, locator: Locator):
        self.driver.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: Locator):
        self.driver.until(EC.element_to_be_clickable(locator))

    def wait_for_located(self, locator: Locator):
        self.driver.until(EC.presence_of_element_located(locator))

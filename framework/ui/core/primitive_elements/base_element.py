from selenium.common.exceptions import TimeoutException

from framework.ui.core.wrappers.common import retry_wrapper
from framework.ui.core.wrappers.element_waiter import ElementWaiter
from framework.ui.core.wrappers.locator import Locator


class BaseElement:

    def __init__(self, web_driver, locator: Locator):
        self._web_driver = web_driver
        self._waiter = ElementWaiter(self._web_driver)
        self.locator = locator

    @property
    def element(self):
        return self._web_driver.find_element(*self.locator)

    @property
    def element_list(self):
        return self._web_driver.find_elements(*self.locator)

    def is_clickable(self):
        try:
            self._waiter.wait_for_clickable(self.locator)
            return True
        except TimeoutException:
            return False

    @retry_wrapper(stop_max_attempt_number=5, wait_fixed=2000, retry_on_result=lambda result: result is None)
    def is_not_clickable(self):
        try:
            self._waiter.wait_for_clickable(self.locator)
        except TimeoutException:
            return True

    def is_visible(self):
        try:
            self._waiter.wait_for_visible(self.locator)
            return True
        except TimeoutException:
            return False

    @retry_wrapper(stop_max_attempt_number=5, wait_fixed=2000, retry_on_result=lambda result: result is None)
    def is_not_visible(self):
        try:
            self._waiter.wait_for_visible(self.locator)
        except TimeoutException:
            return True

    def is_located(self):
        try:
            self._waiter.wait_for_located(self.locator)
            return True
        except TimeoutException:
            return False

    @retry_wrapper(stop_max_attempt_number=5, wait_fixed=2000, retry_on_result=lambda result: result is None)
    def is_not_located(self):
        try:
            self._waiter.wait_for_located(self.locator)
        except TimeoutException:
            return True

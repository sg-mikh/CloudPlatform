import time

from selenium.common.exceptions import TimeoutException

from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.wrappers.element_waiter import ElementWaiter


class Scroller:
    """
    Прокручивает страницу вверх и вниз до нужного элемента.
    """

    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.waiter = ElementWaiter(web_driver, timeout=5)

    def _scroll(self, element: BaseElement, y: int):
        for x in range(5):
            try:
                self.waiter.wait_for_located(element.locator)
                return True
            except TimeoutException:
                self.web_driver.execute_script(f"window.scrollTo(0, {y});")
                time.sleep(1)
                continue
        raise Exception(f"Element with locator {element.locator} doesn't exist")

    def up_to_element(self, element: BaseElement, y: int = None):
        y = abs(y) if y is not None else 250
        self._scroll(element, -y)

    def down_to_element(self, element: BaseElement, y: int = None):
        y = abs(y) if y is not None else 250
        self._scroll(element, y)

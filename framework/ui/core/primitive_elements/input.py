from selenium.webdriver.common.keys import Keys

from framework.ui.core.primitive_elements.base_element import BaseElement


class Input(BaseElement):

    def fill(self, value: str, clear: bool = False):
        if not self.is_visible():
            raise Exception(f'The element with locator {self.locator} is not visible')

        el = self.element
        if clear:
            el.clear()
            el.send_keys(Keys.LEFT_CONTROL + 'a')
            el.send_keys(Keys.BACKSPACE)
            el.send_keys(Keys.COMMAND + 'a')
            el.send_keys(Keys.BACKSPACE)
        el.send_keys(value)

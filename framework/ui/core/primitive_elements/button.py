from framework.ui.core.primitive_elements.base_element import BaseElement


class Button(BaseElement):

    def click(self):
        if not self.is_visible():
            raise Exception(f'The element with locator {self.locator} is not visible')

        if not self.is_clickable():
            raise Exception(f'The element with locator {self.locator} is not clickable')

        self.element.click()

    @property
    def text(self) -> str:
        if not self.is_visible():
            raise Exception(f'The element with locator {self.locator} is not visible')
        return self.element.text

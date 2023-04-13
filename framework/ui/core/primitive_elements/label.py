from framework.ui.core.primitive_elements.base_element import BaseElement


class Label(BaseElement):

    @property
    def text(self) -> str:
        if not self.is_visible():
            raise Exception(f'The element with locator {self.locator} is not visible')
        return self.element.text

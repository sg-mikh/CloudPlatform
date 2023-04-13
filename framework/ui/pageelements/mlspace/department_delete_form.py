from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.wrappers.locator import Locator


class DepartmentDeleteForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def delete_button(self) -> Button:
        return Button(self.base_element,
                      Locator.xpath('.//button[@class="Wrapper-0_0_0-wnpvfju"]/span[contains(text(), "Удалить")]'))

    @property
    def cancel_button(self) -> Button:
        return Button(self.base_element,
                      Locator.xpath('.//button[@class="Wrapper-0_0_0-wnpvfju"]/span[contains(text(), "Отмена")]'))

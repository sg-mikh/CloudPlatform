from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator


class ErrorOnDeleteForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def ok_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('(.//button[@class="Wrapper-0_0_0-wnpvfju"])[1]'))

    @property
    def cancel_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('(.//button[@class="Wrapper-0_0_0-wnpvfju"])[2]'))

    @property
    def message_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[@class="Title-0_0_0-tgrrecl"]'))

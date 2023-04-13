from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.wrappers.locator import Locator


class ServiceAddingForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def mlspace_checkbox(self) -> Button:
        return Button(self.base_element, Locator.xpath('//form/.//div[@class="Wrapper-0_0_0-w1r67slp"]'))

    @property
    def add_service_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('//form/.//button[@class="Wrapper-0_0_0-wnpvfju"]'))

    def add_mlspace(self):
        self.mlspace_checkbox.click()
        self.add_service_button.click()

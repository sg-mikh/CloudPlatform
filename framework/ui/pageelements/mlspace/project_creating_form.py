from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.input import Input
from framework.ui.core.wrappers.locator import Locator


class ProjectCreatingForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def project_name_field(self) -> Input:
        return Input(self.base_element, Locator.xpath('//input[@class="Control-0_0_0-c1qwygaz" and @name="name"]'))

    @property
    def description_field(self) -> Input:
        return Input(self.base_element,
                     Locator.xpath('//input[@class="Control-0_0_0-c1qwygaz" and @name="description"]'))

    @property
    def create_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('//button[@class="Wrapper-0_0_0-wnpvfju"]'))

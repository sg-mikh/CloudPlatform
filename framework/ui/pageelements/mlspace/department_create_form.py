from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.input import Input
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator


class DepartmentCreateForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def name_input(self) -> Input:
        return Input(self.base_element, Locator.xpath('.//input[@name="name"]'))

    @property
    def description_input(self) -> Input:
        return Input(self.base_element, Locator.xpath('.//input[@name="description"]'))

    @property
    def limit_element(self) -> BaseElement:
        return BaseElement(self.base_element, Locator.xpath('.//input[@name="limit"]'))

    @property
    def field_error_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[@class="Error_ecwwbjj"]'))

    @property
    def create_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//button[@class="Wrapper-0_0_0-wnpvfju"]'))

    def is_required_message_visible(self):
        return self.field_error_label.is_visible()

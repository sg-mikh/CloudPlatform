from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator


class ProjectCell:
    """ Соответствует ячейке проекта на странице со списком проектов """

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def name_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[@class="Name-0_0_0-n1xf9s20"]'))

    @property
    def department_name_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[@class="Stat-0_0_0-sp5ai36"]'))

    @property
    def delete_menu_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//button[@class="Wrapper-0_0_0-w5bg5xh"]'))

    @property
    def delete_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//div[@class="Wrapper-0_0_0-wz40qw9"]'))

    def name(self) -> str:
        return self.name_label.text

import datetime
import re

from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator


class DepartmentCell:
    """ Соответствует ячейке департамента на странице со списком департаментов """

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def name_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[@class="Name-0_0_0-n1fwrb3f"]'))

    @property
    def date_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('(.//div[@class="Stat-0_0_0-s13lrino"])[1]'))

    @property
    def limit_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('(.//div[@class="Stat_s13lrino"])[last()]'))

    @property
    def menu_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//button[@class="Wrapper-0_0_0-w5bg5xh"]'))

    @property
    def delete_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//div[@class="Wrapper-0_0_0-wz40qw9"]'))

    def name(self) -> str:
        return self.name_label.text

    def date(self) -> datetime:
        return datetime.datetime.strptime(self.date_label.text, "%d.%m.%Y").date()

    def limit(self):
        el_text = self.limit_label.text
        if el_text.lower() == 'без лимита':
            return el_text

        res = re.search(r"\d+", el_text.replace(" ", "")).group()
        return int(res)

    def delete(self):
        self.menu_button.click()
        self.delete_button.click()

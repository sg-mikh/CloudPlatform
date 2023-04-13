import datetime

from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator


class MlSpaceServiceCard:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def status_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[starts-with(@class, "StatusTag-0_0_0-s1lb2tsh")]'))

    @property
    def activation_date_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('(.//table/.//tr)[last()]/td[last()]'))

    @property
    def open_console_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//a[starts-with(@class, "ToConsole-0_0_0-tkrtg2f")]'))

    def status(self) -> str:
        return self.status_label.text.lower()

    def activation_date(self) -> datetime.date:
        return datetime.datetime.strptime(self.activation_date_label.text, "%d.%m.%Y").date()

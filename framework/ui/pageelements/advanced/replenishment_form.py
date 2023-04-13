from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.input import Input
from framework.ui.core.wrappers.locator import Locator


class ReplenishmentForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def bind_card_button(self) -> Button:
        return Button(self.base_element,
                      Locator.xpath('.//button[starts-with(@class, "buttonClassName-0_0_0-b1acqoe4")]'))

    @property
    def amount_field(self) -> Input:
        return Input(self.base_element, Locator.xpath('.//input[@name="amount"]'))

    @property
    def next_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//div[@class="Action-0_0_0-aj3cqhf"]/button'))

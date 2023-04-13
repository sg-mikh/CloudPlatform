from framework.helpers.wait import wait_while
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.link import Link
from framework.ui.core.wrappers.locator import Locator


class LeftMenu:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def services_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('.//a[@class="active Item-0_0_0-i1s0phzp"]/div'))

    @property
    def doc_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('.//a[@class="Item-0_0_0-i1s0phzp"]/div'))

    @property
    def offer_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('.//a[@class="BottomItem-0_0_0-b1d45uxo"]/div'))

    @property
    def collapse_button(self) -> Button:
        return Button(self.base_element,
                      Locator.xpath('.//button[starts-with(@class,"CollapseIcon-0_0_0-c84muck")]'))

    def is_expanded(self):
        return self.base_element.get_attribute('data-opened') is not None

    def expand(self):
        if wait_while(lambda: self.is_expanded(), 5):
            return
        self.collapse_button.click()

    def collapse(self):
        if wait_while(lambda: self.is_expanded() is False, 5):
            return
        self.collapse_button.click()

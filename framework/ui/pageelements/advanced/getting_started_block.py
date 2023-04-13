from framework.ui.core.primitive_elements.link import Link
from framework.ui.core.wrappers.locator import Locator


class GettingStartedBlock:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def balance_replenishment_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('(.//a[@class="Link-0_0_0-l196qf7p"])[1]'))

    @property
    def test_period_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('(.//a[@class="Link-0_0_0-l196qf7p"])[2]'))

    @property
    def cases_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('(.//a[@class="Link-0_0_0-l196qf7p"])[3]'))

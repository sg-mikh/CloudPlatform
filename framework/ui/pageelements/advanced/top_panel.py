from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.primitive_elements.link import Link
from framework.ui.core.wrappers.locator import Locator


class TopPanel:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def contract_info_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[@class="Center-0_0_0-c1o0qkqw"]/span'))

    @property
    def services_usage_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//a[@class="Button-0_0_0-bc8e1rp"]'))

    @property
    def doc_link(self) -> Link:
        return Link(self.base_element, Locator.xpath('.//div[@class="Icons-0_0_0-it5b8mo"]/a/button'))

    @property
    def profile_menu_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//div[@class="Actions-0_0_0-a1qil317"]/button'))

    @property
    def profile_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('(//div[@class="OptionContent-0_0_0-o173dcaz"])[1]'))

    @property
    def exit_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('(//div[@class="OptionContent-0_0_0-o173dcaz"])[2]'))

    def contract_info(self) -> str:
        return self.contract_info_label.text

    def services_usage_amount(self) -> int:
        text = self.services_usage_button.text
        return int(text.replace(' ', '').replace('₽', '').replace(',', ''))

    def open_profile(self):
        self.profile_menu_button.click()
        self.profile_button.click()

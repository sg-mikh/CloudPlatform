import re

from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageelements.advanced.profile_edit_form import ProfileEditForm


class ProfilePage:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/profile"

    @property
    def name_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Name-0_0_0-nw8yktq"]'))

    @property
    def email_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('(//div[@class="Item-0_0_0-i21wzan"])[1]'))

    @property
    def phone_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('(//div[@class="Item-0_0_0-i21wzan"])[2]'))

    @property
    def edit_profile_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//button[starts-with(@class,"Edit-0_0_0-e1qbf2yo")]'))

    @property
    def contract_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//span[@class="Agreement-0_0_0-az7lsle"]'))

    @property
    def balance_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//h5[@class="Balance-0_0_0-b59c6uj"]'))

    @property
    def balance_description_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//p[@class="Description-0_0_0-d1nagnek"]'))

    @property
    def edit_profile_form(self) -> ProfileEditForm:
        el = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if el.is_not_visible():
            raise Exception(f"Edit profile form not found. Locator: {el.locator}")
        return ProfileEditForm(el.element)

    def name(self) -> str:
        return self.name_label.text

    def email(self) -> str:
        return self.email_label.text

    def phone(self) -> str:
        return self.phone_label.text

    def contract(self) -> str:
        return self.contract_label.text

    def balance(self) -> int:
        text = self.balance_label.text
        res = re.search(r'\d+|^₽', text.replace(' ', '').replace(',', '')).group()
        return int(res)

    def balance_description(self) -> str:
        return self.balance_description_label.text

from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.input import Input
from framework.ui.core.wrappers.locator import Locator


class ProfileEditForm:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def name_field(self) -> Input:
        return Input(self.base_element, Locator.xpath('.//input[@name="firstName"]'))

    @property
    def surname_field(self) -> Input:
        return Input(self.base_element, Locator.xpath('.//input[@name="lastName"]'))

    @property
    def phone_field(self) -> Input:
        return Input(self.base_element, Locator.xpath('.//input[@name="phone"]'))

    @property
    def save_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//button[@class="Wrapper-0_0_0-wnpvfju"]'))

    def replace_profile_info(self, name: str, surname: str):
        self.name_field.fill(name, clear=True)
        self.surname_field.fill(surname, clear=True)
        self.save_button.click()

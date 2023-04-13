from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageelements.mlspace.mlspace_service_card import MlSpaceServiceCard
from framework.ui.pageelements.mlspace.service_adding_form import ServiceAddingForm
from framework.ui.pageobjects.base_page import BasePage


class ProjectPage(BasePage):

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/organization/projects/view/{id}"

    @property
    def service_empty_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Content-0_0_0-c1j5p54g"]'))

    @property
    def add_service_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//button[starts-with(@class, "AddService-0_0_0-agmxpy3")]'))

    @property
    def mlspace_tail(self):
        return BaseElement(self.web_driver, Locator.xpath('//div[@class="Header_h6vq0u7"]'))

    @property
    def service_adding_form(self) -> ServiceAddingForm:
        el = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wq52o8d"]'))
        if el.is_not_visible():
            raise Exception(f"Service adding form not found. Locator: {el.locator}")
        return ServiceAddingForm(el.element)

    @property
    def mlspace_card(self) -> MlSpaceServiceCard:
        card = BaseElement(self.web_driver, Locator.xpath('//div[@class="CardWrapper-0_0_0-c3vfa63"]'))
        if card.is_not_visible():
            raise Exception(f"MlSpace card not found. Locator: {card.locator}")
        return MlSpaceServiceCard(card.element)

    def add_mlspace_service(self):
        self.add_service_button.click()
        form = self.service_adding_form
        form.add_mlspace()

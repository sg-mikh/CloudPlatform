from framework.helpers.wait import wait_while
from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageelements.advanced.getting_started_block import GettingStartedBlock
from framework.ui.pageelements.advanced.left_menu import LeftMenu
from framework.ui.pageelements.advanced.replenishment_form import ReplenishmentForm
from framework.ui.pageelements.advanced.service_card import ServiceCard
from framework.ui.pageelements.advanced.top_panel import TopPanel


class AdvancedMainPage:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/services"

    @property
    def platform_name_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Wrapper-0_0_0-w1wllxxp"]/h2'))

    @property
    def more_info_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//div[@class="Wrapper-0_0_0-w1wllxxp"]/a'))

    @property
    def current_balance_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Wrapper-0_0_0-wht8v5v"]/h1'))

    @property
    def replenish_balance_button(self) -> Button:
        """ Кнопка "Пополнить" """
        return Button(self.web_driver, Locator.xpath('//div[@class="Actions-0_0_0-a1fuo539"]/button'))

    def replenishment_form(self) -> ReplenishmentForm:
        el = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if el.is_not_visible():
            raise Exception(f"Replenishment form not found. Locator: {el.locator}")
        return ReplenishmentForm(el.element)

    def getting_started(self) -> GettingStartedBlock:
        """ Блок "Начало работы" """
        el = BaseElement(self.web_driver, Locator.xpath('//div[@class="Wrapper-0_0_0-w3rbhbe"]'))
        if el.is_not_visible():
            raise Exception(f"Getting started element not found. Locator: {el.locator}")
        return GettingStartedBlock(el.element)

    def left_menu(self) -> LeftMenu:
        left_menu = BaseElement(self.web_driver, Locator.xpath('//nav[@class="Wrapper-0_0_0-w18a6gg9"]'))
        if left_menu.is_not_visible():
            raise Exception(f"Left menu element not found. Locator: {left_menu.locator}")
        return LeftMenu(left_menu.element)

    def top_panel(self) -> TopPanel:
        top_panel = BaseElement(self.web_driver, Locator.xpath('//header[@class="Wrapper-0_0_0-w1562u2o"]'))
        if top_panel.is_not_visible():
            raise Exception(f"Top panel not found. Locator: {top_panel.locator}")
        return TopPanel(top_panel.element)

    def advanced_service_card(self) -> ServiceCard:
        card = BaseElement(self.web_driver, Locator.xpath('//div[starts-with(@class, "Card-0_0_0-c1nwutrq")]'))
        if card.is_not_visible():
            raise Exception(f"Service card not found. Locator: {card.locator}")
        return ServiceCard(card.element)

    def platform_name(self) -> str:
        return self.platform_name_label.text

    def current_balance(self) -> int:
        wait_while(lambda: self.current_balance_label.text != "")
        return int(self.current_balance_label.text.replace(' ', '').replace('₽', '').replace(',', ''))

    def replenish_balance(self, amount: int):
        self.replenish_balance_button.click()
        form = self.replenishment_form()
        form.amount_field.fill(str(amount))
        form.next_button.click()

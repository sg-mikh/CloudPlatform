from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.input import Input
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageobjects.base_page import BasePage


class SberPaymentPage(BasePage):

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/payment/merchants"

    @property
    def card_number_field(self) -> Input:
        return Input(self.web_driver, Locator.xpath('//form//input[@id="pan"]'))

    @property
    def month_year_field(self) -> Input:
        return Input(self.web_driver, Locator.xpath('//form//input[@id="expiry"]'))

    @property
    def cvv_field(self) -> Input:
        return Input(self.web_driver, Locator.xpath('//form//input[@id="cvc"]'))

    @property
    def payment_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//form//button[@data-test-id="submit-payment"]'))

    def is_page_opened(self):
        return self.payment_button.is_visible()

    def payment(self, card_number: str, month: int, year: int, cvv: int):
        self.card_number_field.fill(card_number)
        self.month_year_field.fill(f"{month}{year}")
        self.cvv_field.fill(str(cvv))
        self.payment_button.click()

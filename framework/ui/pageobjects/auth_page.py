from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.input import Input
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageobjects.base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/"

    @property
    def individual_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//div[@data-type="person"]'))

    @property
    def legal_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//div[@data-type="company"]'))

    @property
    def username_field(self) -> Input:
        return Input(self.web_driver, Locator.id("username"))

    @property
    def password_field(self) -> Input:
        return Input(self.web_driver, Locator.id("password"))

    @property
    def login_button(self) -> Button:
        return Button(self.web_driver, Locator.id("kc-login"))

    @property
    def sign_up_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//div[@class="registration-block-content"]/a'))

    @property
    def forget_password_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//a[@class="forget-link"]'))

    @property
    def become_client_button(self) -> Button:
        return Button(self.web_driver, Locator.id('kc-become-client'))

    @property
    def error_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[starts-with(@class,"alert alert_error")]'))

    def sign_in_legal(self, username: str, password: str):
        self.legal_button.click()
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def has_error_message(self) -> bool:
        return self.error_label.is_located() and self.error_label.is_visible()

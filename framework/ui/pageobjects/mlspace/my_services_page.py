from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageobjects.base_page import BasePage


class MyServicesPage(BasePage):

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/services"

    @property
    def limit_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//h1[@class="Amount-0_0_0-a1dw2g2e"]'))

    def current_limit(self) -> int:
        return int(self.limit_label.text.replace(' ', '').replace('₽', ''))

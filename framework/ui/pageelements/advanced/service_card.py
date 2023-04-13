from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator


class ServiceCard:

    def __init__(self, base_element):
        self.base_element = base_element

    @property
    def trial_access_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('.//div[starts-with(@class, "TrialTag-0_0_0-t9hg5zn")]'))

    @property
    def status_label(self) -> Label:
        return Label(self.base_element,
                     Locator.xpath('.//table//div[starts-with(@class, "StatusTag-0_0_0-s1lb2tsh")]'))

    @property
    def expiration_date_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('(.//table//td[@class="Value-0_0_0-v15dm12o"])[2]'))

    @property
    def grant_balance_label(self) -> Label:
        return Label(self.base_element, Locator.xpath('(.//table//td[@class="Value-0_0_0-v15dm12o"])[3]'))

    @property
    def go_to_console_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//a[starts-with(@class,"ToConsole-0_0_0-tkrtg2f")]'))

    @property
    def activate_main_balance_button(self) -> Button:
        return Button(self.base_element, Locator.xpath('.//button[@class="Activate-0_0_0-a1k8n46m"]'))

    def has_trial_access(self):
        try:
            return self.trial_access_label.text.lower() == "тестовый доступ"
        except Exception:
            return False

    def grant_balance(self):
        clear_value = self.grant_balance_label.text.replace(' ', '').replace('₽', '').replace(',', '')
        return int(clear_value)

    def status_text(self):
        return self.status_label.text

    def go_to_console(self):
        self.go_to_console_button.click()

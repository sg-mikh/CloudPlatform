import allure
import pytest

from framework.helpers.wait import wait_while
from framework.testdata.cards import MasterCard
from framework.testdata.users import AdvancedIndividualUser
from framework.ui.pageobjects.advanced.main_page import AdvancedMainPage
from framework.ui.pageobjects.sber_payment_page import SberPaymentPage

REPLENISHMENT_AMOUNT = 150


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Баланс")
class TestBalance:

    @allure.title("Пополение баланса")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualUser])
    def test_replenish_balance(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)
        old_balance = main_page.current_balance()

        with allure.step("Пополнить баланс через форму пополнения"):
            main_page.replenish_balance(REPLENISHMENT_AMOUNT)

        with allure.step("Заполнить форму Сбербанка"):
            browser.switch_to_tab(1)
            sber_payment_page = SberPaymentPage(browser.web_driver)
            card = MasterCard()
            sber_payment_page.payment(card.number, card.month, card.year, card.cvv)
            wait_while(lambda: sber_payment_page.is_page_opened() is False)
            browser.switch_to_tab(0)

        with allure.step("Проверить что баланс изменился"):
            def new_balance():
                browser.refresh()
                return main_page.current_balance()

            assert wait_while(lambda: new_balance() - old_balance == REPLENISHMENT_AMOUNT)

    @pytest.mark.skip("Привязка не работает")
    @allure.title("Привязка карты")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualUser])
    def test_bind_card(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)
        old_balance = main_page.current_balance()

        with allure.step("Перейти на форму привязки карты"):
            main_page.click_replenish_balance()
            replenishment_form = main_page.replenishment_form()
            replenishment_form.click_bind_card()

        with allure.step("Заполнить форму Сбербанка"):
            browser.switch_to_tab(1)
            sber_payment_page = SberPaymentPage(browser.web_driver)
            card = MasterCard()
            sber_payment_page.payment(card.number, card.month, card.year, card.cvv)
            browser.switch_to_tab(0)

        with allure.step("Пополнить с привязанной картой"):
            main_page.replenish_balance(REPLENISHMENT_AMOUNT)

        with allure.step("Проверить что баланс изменился"):
            def new_balance():
                browser.refresh()
                return main_page.current_balance()

            assert wait_while(lambda: new_balance() - old_balance == REPLENISHMENT_AMOUNT, timeout=40)

        with allure.step("Изменить привязанную карту"):
            pass

import allure
import pytest

from framework.testdata.users import AdvancedIndividualNewStateUser
from framework.ui.pageobjects.advanced.main_page import AdvancedMainPage


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Карточка услуги Advanced")
class TestAdvancedServiceCard:

    @allure.title("Состояние карточки по умолчанию")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualNewStateUser])
    def test_default_state(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)

        with allure.step("Проверить информацию по умолчанию"):
            service_card = main_page.advanced_service_card()
            assert service_card.has_trial_access()
            assert service_card.grant_balance() == 10000

        with allure.step("Перейти в консоль"):
            service_card.go_to_console()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("console.hc.sbercloud.ru")
            browser.switch_to_tab(0)

    @pytest.mark.skip("Требуется научиться восстанавливать тестовый доступ")
    @allure.title("Активация основного баланса")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualNewStateUser])
    def test_activate_main_balance(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)
        main_page.current_balance()
        # TODO

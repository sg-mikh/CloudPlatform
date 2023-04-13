import re
import allure
import pytest

from framework.testdata.users import AdvancedIndividualUser, AdvancedIndividualNewUser
from framework.ui.pageobjects.advanced.main_page import AdvancedMainPage


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Компоненты главной страницы")
class TestMainPage:

    @allure.title("Состояние при первом входе")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualNewUser])
    def test_state_on_first_entry(self, browser):
        # TODO проверить pop-up о привязке карты
        pass

    @allure.title("Боковое меню")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualUser])
    def test_left_menu(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)

        with allure.step("Состояние по умолчанию - свернуто"):
            left_menu = main_page.left_menu()
            assert not left_menu.is_expanded()

        with allure.step("Развернуть и свернуть меню"):
            left_menu.expand()
            assert left_menu.is_expanded()
            left_menu.collapse()
            assert not left_menu.is_expanded()

        with allure.step("Переход на документацию и оферту"):
            left_menu.doc_link.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("docs.sbercloud.ru/console/")
            browser.close_current_tab()
            browser.switch_to_tab(0)

            left_menu.offer_link.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("Oferta_na_okazaniye_uslug")
            browser.close_current_tab()
            browser.switch_to_tab(0)

    @allure.title("Проверка блоков на главной странице")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualUser])
    def test_main_page_blocks(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)

        with allure.step("Блок платформа"):
            assert main_page.platform_name().lower() == "платформа sbercloud.advanced"

            main_page.more_info_button.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("/ru/advanced")
            browser.close_current_tab()
            browser.switch_to_tab(0)

        with allure.step("Блок Баланс"):
            assert main_page.current_balance() >= 10000

        with allure.step("Блок Начало работы"):
            main_page.getting_started().balance_replenishment_link.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("guides__payment.html")
            browser.close_current_tab()
            browser.switch_to_tab(0)

            main_page.getting_started().test_period_link.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("test-period.html")
            browser.close_current_tab()
            browser.switch_to_tab(0)

            main_page.getting_started().cases_link.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("/ru/cases")

    @allure.title("Верхняя панель")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualUser])
    def test_top_panel(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)

        with allure.step("Информация о договоре"):
            top_panel = main_page.top_panel()
            assert re.search(r"договор д/д-\w\w/\d\d/\d\d", top_panel.contract_info(), re.IGNORECASE)

        with allure.step("Кнопка потребления услуг"):
            assert main_page.current_balance() == top_panel.services_usage_amount()

        with allure.step("Переход на документацию"):
            top_panel.doc_link.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str("docs.sbercloud.ru/console/")

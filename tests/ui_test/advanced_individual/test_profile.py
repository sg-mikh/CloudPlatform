import re

import allure
import pytest

from framework.helpers.wait import wait_while
from framework.testdata.users import AdvancedIndividualUser
from framework.ui.pageobjects.advanced.main_page import AdvancedMainPage
from framework.ui.pageobjects.advanced.profile_page import ProfilePage


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Профиль")
class TestProfile:

    @allure.title("Проверка компонентов страницы")
    @pytest.mark.parametrize('product_user', [AdvancedIndividualUser])
    def test_profile_page_components(self, browser):
        main_page: AdvancedMainPage = browser.navigate_to(AdvancedMainPage)
        assert browser.is_page_current(AdvancedMainPage)

        with allure.step("Открыть страницу профиля из верхней панели"):
            top_panel = main_page.top_panel()
            top_panel.open_profile()
            assert browser.is_page_current(ProfilePage)

        with allure.step("Основные данные профиля"):
            profile_page: ProfilePage = browser.navigate_to(ProfilePage)
            assert profile_page.name()
            assert profile_page.email().endswith("gmail.com")
            assert profile_page.phone()

        with allure.step("Договор"):
            assert re.search(r"д/д-\w\w/\d\d/\d\d", profile_page.contract(), re.IGNORECASE)

        with allure.step("Баланс"):
            assert wait_while(lambda: profile_page.balance() > 0)

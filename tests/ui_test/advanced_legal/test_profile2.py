import random

import allure
import pytest

from framework.testdata.users import AdvancedLegalUser
from framework.ui.pageobjects.advanced.profile_page import ProfilePage


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Профиль")
class TestProfile:

    @allure.title("Редактирование данных профиля")
    @pytest.mark.parametrize('product_user', [AdvancedLegalUser])
    def test_edit_profile(self, browser):
        profile_page: ProfilePage = browser.navigate_to(ProfilePage)
        assert browser.is_page_current(ProfilePage)
        new_name = f"TestName-{random.randint(100, 999)}"
        new_surname = f"TestSurname-{random.randint(100, 999)}"

        with allure.step("Изменить данные через форму редактирования"):
            profile_page.edit_profile_button.click()
            form = profile_page.edit_profile_form
            form.replace_profile_info(new_name, new_surname)

            browser.refresh()
            assert profile_page.name() == f'{new_name} {new_surname}'

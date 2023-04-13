import allure
import pytest

from framework.testdata.users import AdvancedLegalUser, MLSpaceUser
from framework.ui.pageobjects.auth_page import AuthPage
from framework.ui.pageobjects.mlspace.my_services_page import MyServicesPage


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Авторизация")
class TestAuth:

    @allure.title("Авторизация с валидными данными")
    def test_auth_valid(self, browser_unauthorized):
        auth_page: AuthPage = browser_unauthorized.navigate_to(AuthPage)
        auth_page.sign_in_legal(MLSpaceUser.login, MLSpaceUser.password)

        assert browser_unauthorized.is_page_current(MyServicesPage), "Не удалось пройти авторизацию"

    @allure.title("Авторизация с невалидными данными")
    @pytest.mark.parametrize("login, passw", [
        (AdvancedLegalUser.login, "qwertyui12345"),
        ('invalid_login', 'invalid_pass')
    ])
    def test_auth_invalid(self, browser_unauthorized, login, passw):
        auth_page: AuthPage = browser_unauthorized.navigate_to(AuthPage)
        auth_page.sign_in_legal(login, passw)

        assert auth_page.has_error_message()

    @allure.title("Авторизация с пустыми полями")
    def test_auth_empty_fields(self, browser_unauthorized):
        auth_page: AuthPage = browser_unauthorized.navigate_to(AuthPage)
        auth_page.legal_button.click()
        auth_page.login_button.click()

        assert auth_page.legal_button.is_located()

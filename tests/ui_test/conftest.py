import time

import allure
import pytest

from framework.testdata.users import BaseProductUser
from framework.ui.core.browser import Browser
from framework.ui.pageobjects.auth_page import AuthPage

HOST = "https://console-dev.cp.4cloud.cf"


@pytest.fixture
def browser(product_user: BaseProductUser):
    b = Browser(host=HOST)
    with allure.step("Авторизация"):
        auth_page: AuthPage = b.navigate_to(AuthPage)
        auth_page.sign_in_legal(product_user.login, product_user.password)
    yield b
    time.sleep(2)  # Задержка чтобы успел создаться скрин, в случае падения теста
    b.quit()


@pytest.fixture()
def browser_unauthorized():
    b = Browser(host=HOST)
    yield b
    b.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        b: Browser = item.funcargs.get("browser")
        if b is None:
            b = item.funcargs.get("browser_unauthorized")
        if b:
            allure.attach(
                b.web_driver.get_screenshot_as_png(),
                "Screenshot",
                allure.attachment_type.PNG)
